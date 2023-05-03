import settings
from displayBoard import display_board

def endGame():
    if settings.player_Win:
        print(display_board()+"\nCongratulations. You win! \nThanks for playing.")
    if settings.computer_Win:
        print(display_board() + "\nUnlucky. You have lost! \nThanks for playing.")
    if settings.draw:
        print(display_board() + "\nThe game is a draw.\nThanks for playing.")