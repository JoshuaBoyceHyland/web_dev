import random

from flask import Flask, render_template, session
import DBcm
from model.data import make_deck, init_deck_values
from calcs import calc_total


app = Flask(__name__)


app.secret_key = (
    "kfke hrt'oerj erterutv'rtjv 'oieqrut0345uv 0'34qutv0rutv 'eqrutv equeqtr' u"
)
creds = {
    'host': 'localhost',
    'database': 'BlackJackDB',
    'user': 'josh',
    'password': 'password'
}

deck_values = init_deck_values()  # Global data (which is OK, as this never changes).


def draw():
    """Return a random card from the deck.

    The deck shrinks by 1 and the session updates.
    """
    selection = random.choice(session["deck"])
    session["deck"].remove(selection)
    session.modified = True
    return selection, deck_values[selection]


def random_gamer():    
    with DBcm.UseDatabase(creds) as db:
        SQL = """
        select gamertag from players
        """
        db.execute(SQL)
        tags = db.fetchall()
        tags = [row[0] for row in tags] 
        who = random.choice(tags)
    return who

def update_games_database(gamertag, outcome, isTwentyOne):
    """ updates the game data of specified user"""
    SQL = """
        insert into games
        (gamertag, outcome,21s)
        values
        (%s,%s,%s)      
        """

    with DBcm.UseDatabase(creds) as db:
        db.execute(SQL, (gamertag, outcome, isTwentyOne))

        SQL = """select * from games"""
        db.execute(SQL)
        results = db.fetchall()



def get_winrate(player):
    "gets a players win rate"
    with DBcm.UseDatabase(creds) as db: 
        SQL = """
        select count(*) from games 
        where gamertag = %s and outcome = "Win"
        """
        db.execute(SQL,(player,))
        results = db.fetchone()
        wins = results[0]

        SQL = """
        select count(*) from games 
        where gamertag = %s and outcome = "Loss"
        """
        db.execute(SQL,(player,))
        results = db.fetchone()
        losses = results[0]

        winRate = (wins/(wins + losses)) * 100

        return winRate

def get_highest_win_streak(player):
    """gets a players highest win streak"""
    with DBcm.UseDatabase(creds) as db: 

        SQL = """select outcome from games where gamertag = %s """
        db.execute(SQL,(player,))
        results = db.fetchall()
        
        highestWinStreak = 0; 
        winStreak =0; 
        
        for result in results:
            if "Loss" in result:
                if(highestWinStreak < winStreak):
                     highestWinStreak = winStreak
                winStreak = 0
            else:
                winStreak +=1
            
        if( winStreak != 0):
            if( winStreak > highestWinStreak):
                highestWinStreak = winStreak


    return highestWinStreak

def get_21s(player):
    """gets a player number of 21s from table"""
    with DBcm.UseDatabase(creds) as db: 
        SQL = """select 21s from games where gamertag = %s """
        db.execute(SQL,(player,))
        results = db.fetchall()
        twentyOnesResults = 0
        for result in results:
            if "yes" in result:
                twentyOnesResults+=1
    return twentyOnesResults


def update_gameStats(winrate, high_streak, twenty_ones, gamertag):
    """updates the stats table if there is a gamer tag exist and inserts if none """
    with DBcm.UseDatabase(creds) as db: 
        ## check if user exist first 
        SQL = """select gamertag from gamestats where gamertag = %s """
        db.execute(SQL,(gamertag,))
        result = db.fetchone()
        print(result)
        if result is None:
            SQL = """ 
                insert into gamestats
                (gamertag, winrate, HighestWinStreak, 21s)
                values
                (%s,%s, %s, %s)        
                """
            db.execute(SQL,(gamertag,winrate,high_streak,twenty_ones))
        else:
            SQL = """
            update gamestats 
            set winrate = %s, HighestWinStreak = %s, 21s =%s 
            where gamertag =%s
            """
            db.execute(SQL,(winrate,high_streak,twenty_ones, gamertag))

def get_player_names():
    """gets a list of players names"""
    with DBcm.UseDatabase(creds) as db:
        SQL = """
        select gamertag from players
        """
        db.execute(SQL)
        tags = db.fetchall()
        tags = [row[0] for row in tags] 
    return tags


@app.get("/")
@app.get("/start")
def display_opening_state():
    """(Re)start the game.

    Reset everything, dealing 2 cards each the Dealer and Player.
    """
    session["gamertag"] = "JDawg"
    
    update_gameStats(get_winrate( session["gamertag"]), get_highest_win_streak( session["gamertag"]), get_21s( session["gamertag"]),  session["gamertag"])

    
    session["deck"] = make_deck()
    session["player"] = []
    session["dealer"] = []

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
        update_games_database(session["gamertag"], "Win","yes" )
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

            # update the new card and total
            snippet = render_template(
                "hit.html",
                player_cards=session["player"],
                player_total=str(calc_total(session["player"])),
                dealer_total=calc_total(session["dealer"]),
                
            )
            # display the result box
            snippet+= displayResultMessgage("Player went Bust, Dealer win!")
            # reveal dealer card
            snippet += flip_dealers_cards_plus()
            update_games_database(session["gamertag"], "Loss","no" )
            return snippet
        
        elif player_calc == 21:
            session["game-over"] = True
            
            snippet = render_template(
                "hit.html",
                player_cards=session["player"],
                player_total=str(calc_total(session["player"])),
                dealer_total=calc_total(session["dealer"]),
                
            )
            
            snippet+=displayResultMessgage("Player got 21, Player Wins!")
            snippet+= flip_dealers_cards_plus()
            update_games_database(session["gamertag"], "Win","yes" )
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
        snippet+= displayResultMessgage("Press restart to play again!")
        return snippet



@app.post("/stand")
def process_stand():
    """Process the stand.

    The Player is done (for whatever reason). It's over to the Dealer to do their thing.
    This gets a little complex due the number of "edge-case" possibilities.
    """

        
    
    if session["game-over"] == False:

        session["game-over"] = True
        dealer_calc = calc_total(session["dealer"])
        player_calc = calc_total(session["player"])
        if dealer_calc == 21 and player_calc == 21:
            msg = "Both the Player and Dealer have 21. It's a draw."
            snippet = flip_dealers_cards()
            snippet+=displayResultMessgage(msg)
            update_games_database(session["gamertag"], "Win","yes" ) ## counts as win
            return snippet

        if dealer_calc == 21:
            msg = "The Dealer has 21. The Dealer wins!"
            snippet = flip_dealers_cards()
            snippet+= displayResultMessgage(msg)
            update_games_database(session["gamertag"], "Loss","no" )
            return snippet

        if player_calc == 21:
            msg = f"The Player has 21. The Player Wins"
            snippet = flip_dealers_cards()
            snippet+= displayResultMessgage(msg)
            update_games_database(session["gamertag"], "Win","yes" )
            return snippet

        while True:  # Gulp...
            if player_calc > 21:
                msg = "The Player went bust! The Dealer wins..."
                snippet = flip_dealers_cards()
                snippet+= displayResultMessgage("The Player went bust! The Dealer wins...")
                update_games_database(session["gamertag"], "Loss","no" )
                return snippet
            if dealer_calc > 21:
                snippet = flip_dealers_cards()
                snippet+= displayResultMessgage("The Dealer went bust ! The Player wins...")
                update_games_database(session["gamertag"], "Win","no" )
                return snippet
                
            if dealer_calc > player_calc:
                snippet = flip_dealers_cards()
                snippet+= displayResultMessgage(f"The Dealer wins with a score of {dealer_calc}.")
                update_games_database(session["gamertag"], "Loss","no" )
                return snippet
            if (dealer_calc == player_calc) and (dealer_calc > 16):
                snippet = flip_dealers_cards()
                snippet += displayResultMessgage("It's a draw (nobody wins).")
                update_games_database(session["gamertag"], "Win","no" ) ## counts as win
                return snippet
            if dealer_calc < 17:
                session["dealer"].append(draw())
                dealer_calc = calc_total(session["dealer"])
            else:
                snippet = flip_dealers_cards()
                snippet+=displayResultMessgage(f"The Player wins (against the Dealer's score of {dealer_calc}).")
                return snippet
    snippet = flip_dealers_cards()
    snippet+=displayResultMessgage("Press restart to play again!")
    return snippet


def flip_dealers_cards():
    return render_template(
                "dealers.html ",
                dealer_cards=session["dealer"],
                dealer_total = calc_total(session["dealer"])
            )

"""reveals the dealers cards as an additional return """
def flip_dealers_cards_plus():
    dealersCards = render_template(
            "dealers.html ",
            dealer_cards=session["dealer"],
            dealer_total = calc_total(session["dealer"])
        )
    snippet = f"""<div id = "dealercards"  hx-swap-oob="innerHTML"> {dealersCards} </div> """
    return snippet 

"""display the result box and a desired message t"""
def displayResultMessgage(result_message):
    res = render_template(
                "result.html",
                result = result_message, 
                )
    snippet = f"""<div id = "result"  hx-swap-oob="innerHTML"> {res} </div> """
    return snippet


if __name__ == "__main__":
    app.run(debug=True)
