import re
from displayBoard import display_board
from computerChoice import computerChoice
from gameStatus import playerWin, computerWin, draw

board = [[" " for i in range(3)] for i in range(3)]
display_board(board)

player1 = input("Please choose X or 0: ")
while player1:
    if not re.search("X|0", player1):
        player1 = input("Please choose X or 0: ")
    if player1 == "X" or player1 == "0":
        break

comp = "0"
if player1 == "0":       
    comp = "X"

difficulty = input("Please select game difficulty (easy, medium or hard): ")
while difficulty:
    if not re.search("easy|medium|hard", difficulty):
        difficulty = input("Please enter either 'easy', 'medium' or 'hard' (case sensitive): ")
    if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
        break

player_Win = False
computer_Win = False
while not player_Win and not computer_Win:
    choice = input("Please make your next move: ")
    while choice:
        if not re.search("[012],[012]", choice):        
            choice = input("Please select a row between 0-2 and a column between 0-2 separated by a comma e.g. 0,2: ")
        if board[int(choice[0])][int(choice[2])] != " ":
            choice = input("This space on the grid is already occupied.  Please choose another: ")
        board[int(choice[0])][int(choice[2])] = player1
        break
    
    playerWin(board, player1)

    draw(board)
    
    computerChoice(difficulty, board, player1, comp)

    computerWin(board, comp)

    print("\n" + display_board(board))


