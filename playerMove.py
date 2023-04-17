import re
def playerMove(choice, board, player1):
    while choice:
        if not re.search("[012],[012]", choice):        
            choice = input("Please select a row between 0-2 and a column between 0-2 separated by a comma e.g. 0,2: ")
        if board[int(choice[0])][int(choice[2])] != " ":
            choice = input("This space on the grid is already occupied.  Please choose another: ")
        board[int(choice[0])][int(choice[2])] = player1
        break
