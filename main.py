import settings
from displayBoard import display_board
from computerChoice import computerChoice
from gameStatus import playerWin, computerWin, draw
from options import playerChoice, difficulty, firstOrSecond
from playerMove import playerMove

settings.init()

board = [[" " for i in range(3)] for i in range(3)]
display_board(board)

settings.player1 = input("Please choose X or 0: ")
playerChoice()
settings.comp = "0"
if settings.player1 == "0":       
    settings.comp = "X"

settings.mode = input("Please select game difficulty (easy, medium or hard): ")
difficulty()

settings.turn = input("Would you like to go first? (y/n): ")
firstOrSecond()

while not settings.player_Win and not settings.computer_Win and not settings.draw:
    if settings.turn == "y":
        settings.choice = input("Please make your next move: ")
        playerMove(board)
    
        playerWin(board)
        if settings.player_Win:
            break

        draw(board)
        if settings.draw:
            break        
    
        computerChoice(board)

        computerWin(board)

        print("\n" + display_board(board))
    
    else:
        computerChoice(board)

        computerWin(board)
        if settings.computer_Win:
            break

        draw(board)
        if settings.draw:
            break   

        print("\n" + display_board(board))

        settings.choice = input("Please make your next move: ")
        playerMove(board)
    
        playerWin(board)

if settings.player_Win:
    print(display_board(board)+"\nCongratulations. You win! \nThanks for playing.")
if settings.computer_Win:
    print(display_board(board) + "\nUnlucky. You have lost! \nThanks for playing.")
if settings.draw:
    print(display_board(board) + "\nThe game is a draw.\nThanks for playing.")








