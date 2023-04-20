import re

def playerChoice(player1):
    while player1:
        if not re.search("X|0", player1):
            player1 = input("Please choose X or 0: ")
        if player1 == "X" or player1 == "0":
            break

def difficulty(difficulty):
    while difficulty:
        if not re.search("easy|medium|hard", difficulty):
            difficulty = input("Please enter either 'easy', 'medium' or 'hard' (case sensitive): ")
        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
            break

def firstOrSecond(turn):
    while turn:
        if not re.search("y|n", turn):
            turn = input("Please enter 'y' for yes if you would like to go first or 'n' if you would like to go second: ")
        if turn == "y" or turn == "n":
            break

