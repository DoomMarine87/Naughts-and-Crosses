from displayBoard import display_board
from computerChoice import computerChoice
from gameStatus import playerWin, computerWin, draw
from options import playerChoice, difficulty
from playerMove import playerMove

board = [[" " for i in range(3)] for i in range(3)]
display_board(board)

player1 = input("Please choose X or 0: ")
playerChoice(player1)
comp = "0"
if player1 == "0":       
    comp = "X"

mode = input("Please select game difficulty (easy, medium or hard): ")
difficulty(mode)

player_Win = False
computer_Win = False
while not player_Win and not computer_Win:
    choice = input("Please make your next move: ")
    playerMove(choice, board, player1)
    
    playerWin(board, player1)

    draw(board)
    
    computerChoice(mode, board, player1, comp)

    computerWin(board, comp)

    print("\n" + display_board(board))


