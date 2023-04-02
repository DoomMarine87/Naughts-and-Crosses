from displayBoard import display_board
from sys import exit
def playerWin(board, player1):
    player_Win = False
    if board[0][0] == player1 and board[0][1] == player1 and board[0][2] == player1:
        player_Win = True
    elif board[1][0] == player1 and board[1][1] == player1 and board[1][2] == player1:
        player_Win = True
        exit(display_board(board)+"\nCongratulations. You win! \nThanks for playing.")
    elif board[2][0] == player1 and board[2][1] == player1 and board[2][2] == player1:
        player_Win = True
        exit(display_board(board)+"\nCongratulations. You win! \nThanks for playing.")
    elif board[0][0] == player1 and board[1][0] == player1 and board[2][0] == player1:
        player_Win = True
        exit(display_board(board)+"\nCongratulations. You win! \nThanks for playing.")
    elif board[0][1] == player1 and board[1][1] == player1 and board[2][1] == player1:
        player_Win = True
        exit(display_board(board)+"\nCongratulations. You win! \nThanks for playing.")
    elif board[0][2] == player1 and board[1][2] == player1 and board[2][2] == player1:
        player_Win = True
        exit(display_board(board)+"\nCongratulations. You win! \nThanks for playing.")
    elif board[0][0] == player1 and board[1][1] == player1 and board[2][2] == player1:
        player_Win = True
        exit(display_board(board)+"\nCongratulations. You win! \nThanks for playing.")
    elif board[0][2] == player1 and board[1][1] == player1 and board[2][0] == player1:
        player_Win = True
        exit(display_board(board)+"\nCongratulations. You win! \nThanks for playing.")
    
def computerWin(board, comp):
    computer_Win = False
    if board[0][0] == comp and board[0][1] == comp and board[0][2] == comp:
        computer_Win = True
        exit(display_board(board) + "\nUnlucky. You have lost! \nThanks for playing.")
    elif board[1][0] == comp and board[1][1] == comp and board[1][2] == comp:
        computer_Win = True
        exit(display_board(board) + "\nUnlucky. You have lost! \nThanks for playing.")
    elif board[2][0] == comp and board[2][1] == comp and board[2][2] == comp:
        computer_Win = True
        exit(display_board(board) + "\nUnlucky. You have lost! \nThanks for playing.")
    elif board[0][0] == comp and board[1][0] == comp and board[2][0] == comp:
        computer_Win = True
        exit(display_board(board) + "\nUnlucky. You have lost! \nThanks for playing.")
    elif board[0][1] == comp and board[1][1] == comp and board[2][1] == comp:
        computer_Win = True
        exit(display_board(board) + "\nUnlucky. You have lost! \nThanks for playing.")
    elif board[0][2] == comp and board[1][2] == comp and board[2][2] == comp:
        computer_Win = True
        exit(display_board(board) + "\nUnlucky. You have lost! \nThanks for playing.")
    elif board[0][0] == comp and board[1][1] == comp and board[2][2] == comp:
        computer_Win = True
        exit(display_board(board) + "\nUnlucky. You have lost! \nThanks for playing.")
    elif board[0][2] == comp and board[1][1] == comp and board[2][0] == comp:
        computer_Win = True
        exit(display_board(board) + "\nUnlucky. You have lost! \nThanks for playing.")

def draw(board):
    counter = 9
    for i in board:
        for j in i:
            if j != " ":
                counter -= 1
    
    if counter == 0:
        exit(display_board(board) + "\nThe game is a draw.\nThanks for playing.")
    