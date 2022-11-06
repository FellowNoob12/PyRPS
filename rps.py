# All libraries to be used
import random

# Variables to be used
welcome = "Welcome To PyRPS!"
comp_score = 0
player_score = 0
options = ('r', 'p', 's')
player_won = "Player won!"
comp_won = "Computer won!"
score_tie = "Both player won!"


def main():
    print(f"Current score: Player = {player_score} Computer = {comp_score}")

    asking_the_player = input("Pick from the three (r, p, s) ")
    comp_answer = random.choice(options)

    if asking_the_player == 'r' and comp_answer == 'p':
        print(comp_won)
        comp_score + 1
    elif asking_the_player == 'r' and comp_answer == 's':
        print(player_won)
        player_won + 1
    elif asking_the_player == 'r' and comp_answer == 'r':
        print(score_tie)
        comp_score + 1
        player_score + 1
