import settings
import re

def playerMove():
    settings.choice = input("Please make your next move: ")
    while settings.choice:
        if not re.search("[012],[012]", settings.choice):        
            settings.choice = input("Please select a row between 0-2 and a column between 0-2 separated by a comma e.g. 0,2: ")
        if settings.board[int(settings.choice[0])][int(settings.choice[2])] != " ":
            settings.choice = input("This space on the grid is already occupied.  Please choose another: ")
        settings.board[int(settings.choice[0])][int(settings.choice[2])] = settings.player1
        break
