import random

from model.data import make_deck, init_deck_values
from calcs import calc_total

from flask import Flask, render_template, request, session

app = Flask(__name__)


app.secret_key = (
    "kfke hrt'oerj erterutv'rtjv 'oieqrut0345uv 0'34qutv0rutv 'eqrutv equeqtr' u"
)

# Global data.
deck_values = init_deck_values()


def draw():
    """Select a random card from the deck. The deck shrinks by 1."""
    selection = random.choice(session["deck"])
    session["deck"].remove(selection)
    session.modified = True
    return selection, deck_values[selection]


def set_up_player_and_dealer():
    """sets up the player and dealer for a new game"""
    session["gameOver"] = False
    session["deck"] = make_deck()
    session["player"] = []
    session["dealer"] = []
    session["player"].append(draw())
    session["dealer"].append(draw())
    session["player"].append(draw())
    session["dealer"].append(draw())

@app.get("/")
@app.get("/start")
def display_opening_state():
    
    set_up_player_and_dealer()
    return render_current_page()


@app.post("/stand")
def over_to_the_dealer():

    if(session["gameOver"] == False):
        session["playerStands"] = True
        dealer_draw()
        session["gameOver"] = True
        return determine_game_result()
    else:
        return render_restart_message()


@app.post("/hit")
def select_another_card():
    if(session["gameOver"] == False):
        session["player"].append(draw())
        if(forced_game_over()): # check is game over 
            session["gameOver"] = True
            return determine_game_result()
        else:
            return render_current_page()
    else:
        return render_restart_message()

@app.post("/restart")
def restart_game():
    set_up_player_and_dealer()
    return render_current_page()

    

def render_restart_message():
    """renders the page for period of game where dealers second card is hidden """
    return render_template(
        "start.html",
        playerStands = False,
        player_cards=session["player"],
        player_total= "Press restart to play again!",
        dealer_cards =session["dealer"],
        dealer_total = calc_total(session["dealer"]),
        hiddenCard = "static/cards/back.png",
        title="",
        header="",
        footer="",
        number_of_cards=len(session["deck"]),
    )

def render_current_page():
    """renders the page for period of game where dealers second card is hidden """
    return render_template(
        "start.html",
        playerStands = False,
        player_cards=session["player"],
        player_total=calc_total(session["player"]),
        dealer_cards =session["dealer"],
        dealer_total = session["dealer"][0][-1][0],
        hiddenCard = "static/cards/back.png",
        title="",
        header="",
        footer="",
        number_of_cards=len(session["deck"]),
    )

def forced_game_over():
    """checking if the game should keep going, due to player going bust or getting 21 """
    if(calc_total(session["player"]) >= 21):
        return True; 
    else:
        return False; 


def determine_game_result():
    """check what the result of game should be. win, lose, draw and then returns a template that that shows dealers hidden card"""
    gameOverMessage = ""

    ## draw
    if(calc_total(session["player"]) == calc_total(session["dealer"])):
        gameOverMessage = "Its a draw, you and the dealer have same amount!"
    ## cases for any 21 wins 
    elif(calc_total(session["player"]) == 21):
        
        if(calc_total(session["dealer"]) == 21):
            gameOverMessage = "Draw!"
        else:
            gameOverMessage = "You got 21 and bet the dealer!"
    elif(calc_total(session["dealer"]) == 21):
            gameOverMessage = "You Lose, Dealer got 21!"
    ## bust cases
    elif(calc_total(session["player"]) >21):
        gameOverMessage = "You went bust, you lose!"
    elif( calc_total(session["dealer"]) > 21):
        gameOverMessage = "Dealer went bust, you win!"
    ## general closer to 21
    elif(calc_total(session["player"]) > calc_total(session["dealer"])):
        gameOverMessage = "You Win!"
    else:
        gameOverMessage = "You Lose!"
       


                
    return render_a_gameOver_message(gameOverMessage)
            

def render_a_gameOver_message(gameOverMessage):
    

    return render_template(
        "start.html",
        playerStands = True, 
        player_cards=session["player"],
        player_total=calc_total(session["player"]),
        dealer_cards= session["dealer"],
        gameResult = gameOverMessage,
        hiddenCard = "static/cards/" + session["dealer"][-1][-1][-1],
        dealer_total= calc_total(session["dealer"]),
        title="",
        header="",
        footer="",
        number_of_cards=len(session["deck"]),
    )

def dealer_draw():
    while(calc_total(session["dealer"] )<= 17):
        session["dealer"].append(draw())
        session.modified = True


   
if __name__ == "__main__":
    app.run(debug=True)
