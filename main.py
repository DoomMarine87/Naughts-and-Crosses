import settings
from displayBoard import display_board
from computerChoice import computerChoice
from gameStatus import playerWin, computerWin, draw
from options import playerChoice, difficulty, firstOrSecond
from playerMove import playerMove
from winLoseOrDraw import endGame

settings.init()

display_board()

playerChoice()

difficulty()

firstOrSecond()

while not settings.player_Win and not settings.computer_Win and not settings.draw:
    if settings.turn == "y":
        playerMove()
    
        playerWin()
        if settings.player_Win:
            break

        draw()
        if settings.draw:
            break        
    
        computerChoice()

        computerWin()

        print("\n" + display_board())
    
    else:
        computerChoice()

        computerWin()
        if settings.computer_Win:
            break

        draw()
        if settings.draw:
            break   

        print("\n" + display_board())

        playerMove()
    
        playerWin()

endGame()








