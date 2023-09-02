"""
Define two players = you and the bot
Each player will have a name 
Decide on the rules of the game
    bato > gunting
    gunting > papel
    papel > bato
Play for n rounds
Scores are recorded 
Print the winner
"""
#from sys import argv
from time import sleep
from random import randint

options = {"b":"Bato", "g":"Gunting", "p":"Papel"}
ROUNDS = 5

class Player:
    """ This class represent the player. 

    Player.name         : player's name
    Player.score        : player's current score
    Player.get_score()  : add a poing to Player.score
    """
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_score(self):
        self.score += 1

    ## Welp, it's no longer needed. 
    # def throw_hand(self, option):
    #     if option.lower()[0] not in options:
    #         print("You entered an incorrect option. Please choose [B]ato, [G]unting, or [P]apel")

    #     else:
    #         return option.lower()[0]
        
def decision(player_hand, bot_hand):
    if player_hand == bot_hand:
        return "tie"
    
    if  (player_hand == "g" and bot_hand == "p") or \
        (player_hand == "p" and bot_hand == "b") or \
        (player_hand == "b" and bot_hand == "g"):
        return "win"
    
    else:
        return "lose"
    
if __name__ == "__main__":

    print("Welcome to Bato-Bato Pik Tournament!")

    player_name = input("Please enter your name: ")
    print("Welcome, " + player_name)

    sleep(1)

    # Players
    bida = Player(player_name)
    kontrabida = Player("Master Bot")

    for i in range(ROUNDS):
        # Choose [B]ato, [G]unting, or [P]apel. It's case insensitive. Initial letter can be an input
        player_hand = input("Please choose [B]ato, [G]unting, or [P]apel: ")
        bot_hand = list(options.keys())[randint(0, 2)] # bot chooses randomly
        player_hand = player_hand.lower()[0]

        # For invalid throws, give the point to bot
        if player_hand not in options.keys():
            print("What's that? It's not a valid hand for bato-bato pik. Bot got the point.")
            kontrabida.score += 1
            continue # skip round
        
        # Get result of the round
        result = decision(player_hand, bot_hand)

        # Print option selected
        print("You have selected " + options[player_hand])
        print("Bot has selected " + options[bot_hand])
        
        # Give point to the winner
        if result == "win":
            bida.get_score()
            print("You won!")

        elif result == "lose":
            kontrabida.get_score()
            print("You lose!")

        else:
            print("No one wins. It's a tie")

    # Print final scores
    print(f"Your final score is {bida.score}.")
    print(f"Master Bot's final score is {kontrabida.score}.")

    # Print tournament results
    if bida.score > kontrabida.score:
        print("You won the tournament! You defeated Master Bot! Congratulations.")

    elif bida.score < kontrabida.score:
        print("You lost the tournament! Master Bot defeated you!")

    else:
        print("No one won the tournament.")

    print("Game has ended")