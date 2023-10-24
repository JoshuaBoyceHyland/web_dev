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


@app.get("/")
@app.get("/start")
def display_opening_state():
    session["deck"] = make_deck()
    session["playerStands"] = False
    session["player"] = []
    session["dealer"] = []
    session["player"].append(draw())
    session["dealer"].append(draw())
    session["player"].append(draw())
    session["dealer"].append(draw())
    return render_template(
        "start.html",
        player_cards=session["player"],   
        player_total=calc_total(session["player"]),
        dealer_cards=session["dealer"],
        dealer_total= session["dealer"][0][-1][0],
        hiddenCard = "static/cards/back.png",
        title="",
        header="",
        footer="",
        number_of_cards=len(session["deck"]),
    )


@app.post("/stand")
def over_to_the_dealer():
    session["playerStands"] = True
    dealer_draw()
    return render_a_gameOver()

@app.post("/hit")
def select_another_card():
    session["player"].append(draw())
    
    if(forced_game_over()): # check is game over 
        return render_a_gameOver()
    else:
        return render_template(
        "start.html",
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


def render_a_gameOver():

    gameOverMessage = ""
    if(calc_total(session["player"]) == 21):# player got 21, if dealer is equal, if dealer less
        
        if(calc_total(session["dealer"]) == 21):
            gameOverMessage = "You and the dealer have drawn at 21!"
        else:
            gameOverMessage = "You got 21 and bet the dealer!"

    else:
        if(calc_total(session["dealer"]) < 21):
            if(calc_total(session["dealer"]) < calc_total(session["player"])): # if the dealer is greater than player
                gameOverMessage = "You got closer to 21 and won!"
            else:
                gameOverMessage = "The Dealer got closer to 21 and you lost!"
    return render_a_gameOver_message(gameOverMessage)
               

def dealer_draw():
    while(calc_total(session["dealer"] )<= 17):
        session["dealer"].append(draw())
        session.modified = True


         


def render_a_loss():

    return render_template(
        "start.html",
        player_cards=session["player"],
        player_total="You went gotboyce over 21 and went bust",
        dealer_cards=session["dealer"],
        hiddenCard = "static/cards/" + session["dealer"][-1][-1][-1],
        dealer_total= calc_total(session["dealer"]),
        title="",
        header="",
        footer="",
        number_of_cards=len(session["deck"]),
    )

def render_a_gameOver_message(gameOverMessage):
    

    return render_template(
        "start.html",
        playerStands = session["playerStands"], 
        player_cards=session["player"],
        player_total=gameOverMessage,
        dealer_cards= session["dealer"],
        hiddenCard = "static/cards/" + session["dealer"][-1][-1][-1],
        dealer_total= calc_total(session["dealer"]),
        title="",
        header="",
        footer="",
        number_of_cards=len(session["deck"]),
    )

def render_a_win():
    winMessage = " You got 21 congratulations !"
    if(calc_total(session["player"] == calc_total(session["dealer"]))):
       winMessage = "Its a draw, you and the dealer got 21"


    return render_template(
        "start.html",
        player_cards=session["player"],
        player_total=winMessage,
        dealer_cards=session["dealer"],
        hiddenCard = "static/cards/" + session["dealer"][-1][-1][-1],
        dealer_total= calc_total(session["dealer"]),
        title="",
        header="",
        footer="",
        number_of_cards=len(session["deck"]),
    )




    
if __name__ == "__main__":
    app.run(debug=True)
