import settings 
import re


def playerChoice():
    while settings.player1:
        if not re.search("X|0", settings.player1):
            settings.player1 = input("You have not entered 'X' or '0'.  Please choose X or 0 (case sensitive): ")
        if settings.player1 == "X" or settings.player1 == "0":
            break

def difficulty():
    while settings.mode:
        if not re.search("easy|medium|hard", settings.mode):
            settings.mode = input("Please enter either 'easy', 'medium' or 'hard' (case sensitive): ")
        if settings.mode == "easy" or settings.mode == "medium" or settings.mode == "hard":
            break

def firstOrSecond():
    while settings.turn:
        if not re.search("y|n", settings.turn):
            settings.turn = input("Please enter 'y' for yes if you would like to go first or 'n' if you would like to go second: ")
        if settings.turn == "y" or settings.turn == "n":
            break

