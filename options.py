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

