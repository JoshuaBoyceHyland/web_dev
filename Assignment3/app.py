import random

from flask import Flask, render_template, session

from model.data import make_deck, init_deck_values
from calcs import calc_total


app = Flask(__name__)


app.secret_key = (
    "kfke hrt'oerj erterutv'rtjv 'oieqrut0345uv 0'34qutv0rutv 'eqrutv equeqtr' u"
)


deck_values = init_deck_values()  # Global data (which is OK, as this never changes).


def draw():
    """Return a random card from the deck.

    The deck shrinks by 1 and the session updates.
    """
    selection = random.choice(session["deck"])
    session["deck"].remove(selection)
    session.modified = True
    return selection, deck_values[selection]


@app.get("/")
@app.get("/start")
def display_opening_state():
    """(Re)start the game.

    Reset everything, dealing 2 cards each the Dealer and Player.
    """
    session["deck"] = make_deck()

    session["player"] = []
    session["dealer"] = []
    session["can-hit"] = True
    session["can-stand"] = True
    session["player-blackjack"] = False
    session["game-over"] = False

    session["player"].append(draw())
    session["dealer"].append(draw())
    session["player"].append(draw())
    session["dealer"].append(draw())

    opening_message = ""
    player_opening_score = calc_total(session["player"])

    dealer_total_message = session["dealer"][0][-1][0]
    # if first card is an ace it will always be worth 11, 
    # prevents a list with 2 values being returned
    if( type(session["dealer"][0][-1][0]) == list):
        dealer_total_message = 11
    

    snippet = render_template(
        "start.html",
        player_cards=session["player"],
        player_total=player_opening_score,
        dealer_cards=session["dealer"],
        dealer_total= dealer_total_message,
        title="Blackjack for the Web",
        header="Welcome to Blackjack for the Web",
        footer=opening_message,
        )
    if player_opening_score == 21:
        session["can-hit"] = False
        session["game-over"] = True
    
        snippet+=displayResultMessgage("BlackJack, Player Wins")
        return snippet
        
    return snippet


@app.post("/hit")
def process_hit():
    """Process the hit.

    Returning only the snippet of HTML required to update the Player's section of the
    webpage.  Update the can-hit and can-stand booleans as necessary.
    """
    if session["game-over"] == False:
        session["player"].append(draw())
        player_calc = calc_total(session["player"])

        if player_calc > 21:
            session["game-over"] = True
            session["can-hit"] = False
            session["can-stand"] = False

            # update the new card and total
            snippet = render_template(
                "hit.html",
                player_cards=session["player"],
                player_total=str(calc_total(session["player"])),
                dealer_total=calc_total(session["dealer"]),
                
            )
            # display the result box
            snippet+= displayResultMessgage("Player went Bust, \n Dealer win!")
            # reveal dealer card
            snippet += revealDealersCards()

            return snippet
        
        elif player_calc == 21:
            session["can-hit"] = False
            session["game-over"] = True
            snippet = render_template(
                "hit.html",
                player_cards=session["player"],
                player_total=str(calc_total(session["player"])),
                dealer_total=calc_total(session["dealer"]),
                
            )
            
            snippet+=displayResultMessgage("Player got 21, Player Wins!")
            snippet+= revealDealersCards()

            return snippet
        else:
            return render_template(
                "hit.html",
                player_cards=session["player"],
                player_total=str(calc_total(session["player"])),
                dealer_total=calc_total(session["dealer"]),
                
            )
    else:

        snippet = render_template(
                "hit.html",
                player_cards=session["player"],
                player_total=str(calc_total(session["player"])),
                dealer_total=calc_total(session["dealer"]),
                
            )
        snippet+= displayResultMessgage("Press restart to player again!")
        return snippet



@app.post("/stand")
def process_stand():
    """Process the stand.

    The Player is done (for whatever reason). It's over to the Dealer to do their thing.
    This gets a little complex due the number of "edge-case" possibilities.
    """

    def generate_dealer_snippet(msg):
        """This nested function returns the snippt of HTML to update the Dealer's cards."""
        snippet = render_template(
            "dealers.html ",
            dealer_cards=session["dealer"],
            dealer_message=msg,
        )

        return (
            snippet + f"""<div id = "result"  hx-swap-oob="innerHTML"> {render_template("result.html")} </div>"""
        )

    if session["can-stand"]:
        session["can-hit"] = False
        session["can-stand"] = False
        session["game-over"] = True
        dealer_calc = calc_total(session["dealer"])
        player_calc = calc_total(session["player"])

        if dealer_calc == 21 and player_calc == 21:
            msg = "Both the Player and Dealer have 21. It's a draw."
            return generate_dealer_snippet(msg)

        if dealer_calc == 21:
            msg = "The Dealer has 21. The Dealer wins!"
            return generate_dealer_snippet(msg)

        if player_calc == 21:
            msg = f"The Player has 21. The Player Wins"
            return generate_dealer_snippet(msg)

        while True:  # Gulp...
            if player_calc > 21:
                return generate_dealer_snippet(
                    f"The Player went bust! The Dealer wins..."
                )
            if dealer_calc > 21:
                return generate_dealer_snippet(
                    f"The Dealer went bust ! The Player wins..."
                )
            if dealer_calc > player_calc:
                return generate_dealer_snippet(
                    f"The Dealer wins with a score of {dealer_calc}."
                )
            if (dealer_calc == player_calc) and (dealer_calc > 16):
                return generate_dealer_snippet("It's a draw (nobody wins).")
            if dealer_calc < 17:
                session["dealer"].append(draw())
                dealer_calc = calc_total(session["dealer"])
            else:
                return generate_dealer_snippet(
                    f"The Player wins (against the Dealer's score of {dealer_calc})."
                )
    return generate_dealer_snippet("The game is over. Please start again...")


"""reveals the dealers cards"""
def revealDealersCards():
    dealersCards = render_template(
            "dealers.html ",
            dealer_cards=session["dealer"],
            dealer_total = calc_total(session["dealer"])
        )
    snippet = f"""<div id = "dealercards"  hx-swap-oob="innerHTML"> {dealersCards} </div> """
    return snippet 

"""display the result box and a desired message"""
def displayResultMessgage(result_message):
    res = render_template(
                "result.html",
                result = result_message, 
                )
    snippet = f"""<div id = "result"  hx-swap-oob="innerHTML"> {res} </div> """
    return snippet


if __name__ == "__main__":
    app.run(debug=True)
