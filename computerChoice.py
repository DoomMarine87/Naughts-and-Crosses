import random
import settings
def computerChoice(board):
    res = random.randint(1,4)
    if settings.mode == "easy" and res == 1 or settings.mode == "medium" and res == 3 or res == 4 or settings.mode == "hard" and res == 2 or res == 3 or res == 4:
        if board[0][0] == settings.comp and board[0][1] == settings.comp and board[0][2] == " ":
            board[0][2] = settings.comp
            compChoice = "0,2"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][1] == settings.comp and board[0][2] == settings.comp and board[0][0] == " ":
            board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][0] == settings.comp and board[0][2] == settings.comp and board[0][1] == " ":
            board[0][1] = settings.comp
            compChoice = "0,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][0] == settings.comp and board[1][1] == settings.comp and board[1][2] == " ":
            board[1][2] = settings.comp
            compChoice = "1,2"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][1] == settings.comp and board[1][2] == settings.comp and board[1][0] == " ":
            board[1][0] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][0] == settings.comp and board[1][2] == settings.comp and board[1][1] == " ":
            board[1][1] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[2][0] == settings.comp and board[2][1] == settings.comp and board[2][2] == " ":
            board[2][2] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif board[2][1] == settings.comp and board[2][2] == settings.comp and board[2][0] == " ":
            board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[2][0] == settings.comp and board[2][2] == settings.comp and board[2][1] == " ":
            board[2][1] = settings.comp
            compChoice = "2,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][0] == settings.comp and board[1][0] == settings.comp and board[2][0] == " ":
            board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][0] == settings.comp and board[2][0] == settings.comp and board[0][0] == " ":
            board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][0] == settings.comp and board[2][0] == settings.comp and board[1][0] == " ":
            board[1][0] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][1] == settings.comp and board[1][1] == settings.comp and board[2][1] == " ":
            board[2][1] = settings.comp
            compChoice = "2,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][1] == settings.comp and board[2][1] == settings.comp and board[0][1] == " ":
            board[0][1] = settings.comp
            compChoice = "0,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][1] == settings.comp and board[2][1] == settings.comp and board[1][1] == " ":
            board[1][1] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][2] == settings.comp and board[1][2] == settings.comp and board[2][2] == " ":
            board[1][1] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][2] == settings.comp and board[2][2] == settings.comp and board[0][2] == " ":
            board[0][2] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][2] == settings.comp and board[2][2] == settings.comp and board[1][2] == " ":
            board[1][2] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][2] == settings.comp and board[1][1] == settings.comp and board[2][0] == " ":
            board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][0] == settings.comp and board[1][1] == settings.comp and board[2][2] == " ":
            board[2][2] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][2] == settings.comp and board[2][0] == settings.comp and board[1][1] == " ":
            board[1][1] = settings.comp
            compChoice = "1,1"  
            print(f'The Computer chooses: {compChoice}')  
        elif board[1][1] == settings.comp and board[2][2] == settings.comp and board[0][0] == " ":
            board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][2] == settings.comp and board[1][1] == settings.comp and board[2][0] == " ":
            board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][1] == settings.comp and board[2][0] == settings.comp and board[0][2] == " ":
            board[0][2] = settings.comp
            compChoice = "0,2"
            print(f'The Computer chooses: {compChoice}') 
        elif board[0][2] == settings.comp and board[2][0] == settings.comp and board[1][1] == " ":
            board[1][1] = settings.comp
            compChoice = "0,2"    
            print(f'The Computer chooses: {compChoice}') 

        elif board[0][0] == settings.player1 and board[0][1] == settings.player1 and board[0][2] == " ":
            board[0][2] = settings.comp
            compChoice = "0,2"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][1] == settings.player1 and board[0][2] == settings.player1 and board[0][0] == " ":
            board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][0] == settings.player1 and board[0][2] == settings.player1 and board[0][1] == " ":
            board[0][1] = settings.comp
            compChoice = "0,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][0] == settings.player1 and board[1][1] == settings.player1 and board[1][2] == " ":
            board[1][2] = settings.comp
            compChoice = "1,2"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][1] == settings.player1 and board[1][2] == settings.player1 and board[1][0] == " ":
            board[1][0] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][0] == settings.player1 and board[1][2] == settings.player1 and board[1][1] == " ":
            board[1][1] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[2][0] == settings.player1 and board[2][1] == settings.player1 and board[2][2] == " ":
            board[2][2] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif board[2][1] == settings.player1 and board[2][2] == settings.player1 and board[2][0] == " ":
            board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[2][0] == settings.player1 and board[2][2] == settings.player1 and board[2][1] == " ":
            board[2][1] = settings.comp
            compChoice = "2,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][0] == settings.player1 and board[1][0] == settings.player1 and board[2][0] == " ":
            board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][0] == settings.player1 and board[2][0] == settings.player1 and board[0][0] == " ":
            board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][0] == settings.player1 and board[2][0] == settings.player1 and board[1][0] == " ":
            board[1][0] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][1] == settings.player1 and board[1][1] == settings.player1 and board[2][1] == " ":
            board[2][1] = settings.comp
            compChoice = "2,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][1] == settings.player1 and board[2][1] == settings.player1 and board[0][1] == " ":
            board[0][1] = settings.comp
            compChoice = "0,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][1] == settings.player1 and board[2][1] == settings.player1 and board[1][1] == " ":
            board[1][1] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][2] == settings.player1 and board[1][2] == settings.player1 and board[2][2] == " ":
            board[1][1] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][2] == settings.player1 and board[2][2] == settings.player1 and board[0][2] == " ":
            board[0][2] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][2] == settings.player1 and board[2][2] == settings.player1 and board[1][2] == " ":
            board[1][2] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][2] == settings.player1 and board[1][1] == settings.player1 and board[2][0] == " ":
            board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][0] == settings.player1 and board[1][1] == settings.player1 and board[2][2] == " ":
            board[2][2] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][2] == settings.player1 and board[2][0] == settings.player1 and board[1][1] == " ":
            board[1][1] = settings.comp
            compChoice = "1,1"    
            print(f'The Computer chooses: {compChoice}')
        elif board[1][1] == settings.player1 and board[2][2] == settings.player1 and board[0][0] == " ":
            board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[0][2] == settings.player1 and board[1][1] == settings.player1 and board[2][0] == " ":
            board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif board[1][1] == settings.player1 and board[2][0] == settings.player1 and board[0][2] == " ":
            board[0][2] = settings.comp
            compChoice = "0,2"
            print(f'The Computer chooses: {compChoice}') 
        elif board[0][2] == settings.player1 and board[2][0] == settings.player1 and board[1][1] == " ":
            board[1][1] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')

        elif board[1][1] == " ":
            board[1][1] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')

        elif board[0][0] == " " or board[0][2] == " " or board[2][0] == " " or board[2][2] == " ":
            corners = ["0,0","0,2","2,0","2,2"]
            compChoice = random.choice(corners)
            while board[int(compChoice[0])][int(compChoice[2])] != " ":
                compChoice = random.choice(corners)
            board[int(compChoice[0])][int(compChoice[2])] = settings.comp
            print(f'The Computer chooses: {compChoice}')
        
        else:
            compChoice = str(random.randint(0,2)) + "," + str(random.randint(0,2))
            while board[int(compChoice[0])][int(compChoice[2])] != " ":
                compChoice = str(random.randint(0, 2)) + "," + str(random.randint(0,2))
            board[int(compChoice[0])][int(compChoice[2])] = settings.comp
            print(f'The Computer chooses: {compChoice}')
    
    elif settings.mode == "easy" and res == 2 or res == 3 or res == 4 or settings.mode == "medium" and res == 1 or res == 2 or settings.mode == "hard" and res == 1:
        compChoice = str(random.randint(0,2)) + "," + str(random.randint(0,2))
        while board[int(compChoice[0])][int(compChoice[2])] != " ":
            compChoice = str(random.randint(0, 2)) + "," + str(random.randint(0,2))
        board[int(compChoice[0])][int(compChoice[2])] = settings.comp
        print(f'The Computer chooses: {compChoice}')