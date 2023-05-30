def init():
    global board
    board  = [[" " for i in range(3)] for i in range(3)]
    global player1
    player1 = ""
    global comp 
    comp = "0"
    global mode 
    mode = ""
    global turn
    turn = ""
    global player_Win
    player_Win = False
    global computer_Win
    computer_Win = False
    global choice 
    choice = ""
    global draw 
    draw = False
    global playerScore
    playerScore = 0
    global computerScore
    computerScore = 0
    global playAgain
    playAgain = ""
    global stop 
    stop = False
