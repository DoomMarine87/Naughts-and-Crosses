import settings
import re
def playerMove(board):
    while settings.choice:
        if not re.search("[012],[012]", settings.choice):        
            settings.choice = input("Please select a row between 0-2 and a column between 0-2 separated by a comma e.g. 0,2: ")
        if board[int(settings.choice[0])][int(settings.choice[2])] != " ":
            settings.choice = input("This space on the grid is already occupied.  Please choose another: ")
        board[int(settings.choice[0])][int(settings.choice[2])] = settings.player1
        break
