import settings

def playerWin():
    if settings.board[0][0] == settings.player1 and settings.board[0][1] == settings.player1 and settings.board[0][2] == settings.player1:
        settings.player_Win = True
    elif settings.board[1][0] == settings.player1 and settings.board[1][1] == settings.player1 and settings.board[1][2] == settings.player1:
        settings.player_Win = True
    elif settings.board[2][0] == settings.player1 and settings.board[2][1] == settings.player1 and settings.board[2][2] == settings.player1:
        settings.player_Win = True
    elif settings.board[0][0] == settings.player1 and settings.board[1][0] == settings.player1 and settings.board[2][0] == settings.player1:
        settings.player_Win = True
    elif settings.board[0][1] == settings.player1 and settings.board[1][1] == settings.player1 and settings.board[2][1] == settings.player1:
        settings.player_Win = True
    elif settings.board[0][2] == settings.player1 and settings.board[1][2] == settings.player1 and settings.board[2][2] == settings.player1:
        settings.player_Win = True
    elif settings.board[0][0] == settings.player1 and settings.board[1][1] == settings.player1 and settings.board[2][2] == settings.player1:
        settings.player_Win = True
    elif settings.board[0][2] == settings.player1 and settings.board[1][1] == settings.player1 and settings.board[2][0] == settings.player1:
        settings.player_Win = True
    
def computerWin():
    if settings.board[0][0] == settings.comp and settings.board[0][1] == settings.comp and settings.board[0][2] == settings.comp:
        settings.computer_Win = True
    elif settings.board[1][0] == settings.comp and settings.board[1][1] == settings.comp and settings.board[1][2] == settings.comp:
        settings.computer_Win = True
    elif settings.board[2][0] == settings.comp and settings.board[2][1] == settings.comp and settings.board[2][2] == settings.comp:
        settings.computer_Win = True
    elif settings.board[0][0] == settings.comp and settings.board[1][0] == settings.comp and settings.board[2][0] == settings.comp:
        settings.computer_Win = True
    elif settings.board[0][1] == settings.comp and settings.board[1][1] == settings.comp and settings.board[2][1] == settings.comp:
        settings.computer_Win = True
    elif settings.board[0][2] == settings.comp and settings.board[1][2] == settings.comp and settings.board[2][2] == settings.comp:
        settings.computer_Win = True
    elif settings.board[0][0] == settings.comp and settings.board[1][1] == settings.comp and settings.board[2][2] == settings.comp:
        settings.computer_Win = True
    elif settings.board[0][2] == settings.comp and settings.board[1][1] == settings.comp and settings.board[2][0] == settings.comp:
        settings.computer_Win = True

def draw():
    counter = 9
    for i in settings.board:
        for j in i:
            if j != " ":
                counter -= 1
    
    if counter == 0:
        settings.draw = True
    