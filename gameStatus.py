import settings

def playerWin(board):
    if board[0][0] == settings.player1 and board[0][1] == settings.player1 and board[0][2] == settings.player1:
        settings.player_Win = True
    elif board[1][0] == settings.player1 and board[1][1] == settings.player1 and board[1][2] == settings.player1:
        settings.player_Win = True
    elif board[2][0] == settings.player1 and board[2][1] == settings.player1 and board[2][2] == settings.player1:
        settings.player_Win = True
    elif board[0][0] == settings.player1 and board[1][0] == settings.player1 and board[2][0] == settings.player1:
        settings.player_Win = True
    elif board[0][1] == settings.player1 and board[1][1] == settings.player1 and board[2][1] == settings.player1:
        settings.player_Win = True
    elif board[0][2] == settings.player1 and board[1][2] == settings.player1 and board[2][2] == settings.player1:
        settings.player_Win = True
    elif board[0][0] == settings.player1 and board[1][1] == settings.player1 and board[2][2] == settings.player1:
        settings.player_Win = True
    elif board[0][2] == settings.player1 and board[1][1] == settings.player1 and board[2][0] == settings.player1:
        settings.player_Win = True
    
def computerWin(board):
    if board[0][0] == settings.comp and board[0][1] == settings.comp and board[0][2] == settings.comp:
        settings.computer_Win = True
    elif board[1][0] == settings.comp and board[1][1] == settings.comp and board[1][2] == settings.comp:
        settings.computer_Win = True
    elif board[2][0] == settings.comp and board[2][1] == settings.comp and board[2][2] == settings.comp:
        settings.computer_Win = True
    elif board[0][0] == settings.comp and board[1][0] == settings.comp and board[2][0] == settings.comp:
        settings.computer_Win = True
    elif board[0][1] == settings.comp and board[1][1] == settings.comp and board[2][1] == settings.comp:
        settings.computer_Win = True
    elif board[0][2] == settings.comp and board[1][2] == settings.comp and board[2][2] == settings.comp:
        settings.computer_Win = True
    elif board[0][0] == settings.comp and board[1][1] == settings.comp and board[2][2] == settings.comp:
        settings.computer_Win = True
    elif board[0][2] == settings.comp and board[1][1] == settings.comp and board[2][0] == settings.comp:
        settings.computer_Win = True

def draw(board):
    counter = 9
    for i in board:
        for j in i:
            if j != " ":
                counter -= 1
    
    if counter == 0:
        settings.draw = True
    