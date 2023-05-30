import settings
from displayBoard import display_board
import re

def endGame():
    if settings.player_Win:
        settings.playerScore += 1
        print(display_board(), "\nCongratulations. You win!\n \nThanks for playing.\n")
    if settings.computer_Win:
        settings.computerScore += 1
        print(display_board(), "\nUnlucky. You have lost!\n \nThanks for playing.\n")
    if settings.draw:
        print(display_board(), "\nThe game is a draw.\n \nThanks for playing.\n")
    print(f'The score is: Player {settings.playerScore} - {settings.computerScore} Computer\n')

    settings.player_Win = False
    settings.computer_Win = False
    settings.draw = False

    settings.board  = [[" " for i in range(3)] for i in range(3)]

    settings.playAgain = input("Would you like to play again? (y/n): ")
    while settings.playAgain:
        if not re.search("y|n", settings.playAgain):
            settings.playAgain = input("Please type \"y\" for if you wish to play again or \"n\" if you wish to end the game: ")
        break

    if settings.playAgain == "n":
        settings.stop = True

def finish():
    if settings.playAgain == "n":
        print("\nThanks for playing.\n")
        print(f'The score was: Player {settings.playerScore} - {settings.computerScore} Computer\n')

        