import random
import settings

def computerChoice():
    res = random.randint(1,4)
    if settings.mode == "easy" and res == 1 or settings.mode == "medium" and res == 3 or res == 4 or settings.mode == "hard" and res == 2 or res == 3 or res == 4:
        if settings.board[0][0] == settings.comp and settings.board[0][1] == settings.comp and settings.board[0][2] == " ":
            settings.board[0][2] = settings.comp
            compChoice = "0,2"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][1] == settings.comp and settings.board[0][2] == settings.comp and settings.board[0][0] == " ":
            settings.board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][0] == settings.comp and settings.board[0][2] == settings.comp and settings.board[0][1] == " ":
            settings.board[0][1] = settings.comp
            compChoice = "0,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][0] == settings.comp and settings.board[1][1] == settings.comp and settings.board[1][2] == " ":
            settings.board[1][2] = settings.comp
            compChoice = "1,2"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][1] == settings.comp and settings.board[1][2] == settings.comp and settings.board[1][0] == " ":
            settings.board[1][0] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][0] == settings.comp and settings.board[1][2] == settings.comp and settings.board[1][1] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[2][0] == settings.comp and settings.board[2][1] == settings.comp and settings.board[2][2] == " ":
            settings.board[2][2] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[2][1] == settings.comp and settings.board[2][2] == settings.comp and settings.board[2][0] == " ":
            settings.board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[2][0] == settings.comp and settings.board[2][2] == settings.comp and settings.board[2][1] == " ":
            settings.board[2][1] = settings.comp
            compChoice = "2,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][0] == settings.comp and settings.board[1][0] == settings.comp and settings.board[2][0] == " ":
            settings.board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][0] == settings.comp and settings.board[2][0] == settings.comp and settings.board[0][0] == " ":
            settings.board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][0] == settings.comp and settings.board[2][0] == settings.comp and settings.board[1][0] == " ":
            settings.board[1][0] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][1] == settings.comp and settings.board[1][1] == settings.comp and settings.board[2][1] == " ":
            settings.board[2][1] = settings.comp
            compChoice = "2,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][1] == settings.comp and settings.board[2][1] == settings.comp and settings.board[0][1] == " ":
            settings.board[0][1] = settings.comp
            compChoice = "0,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][1] == settings.comp and settings.board[2][1] == settings.comp and settings.board[1][1] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][2] == settings.comp and settings.board[1][2] == settings.comp and settings.board[2][2] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][2] == settings.comp and settings.board[2][2] == settings.comp and settings.board[0][2] == " ":
            settings.board[0][2] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][2] == settings.comp and settings.board[2][2] == settings.comp and settings.board[1][2] == " ":
            settings.board[1][2] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][2] == settings.comp and settings.board[1][1] == settings.comp and settings.board[2][0] == " ":
            settings.board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][0] == settings.comp and settings.board[1][1] == settings.comp and settings.board[2][2] == " ":
            settings.board[2][2] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][2] == settings.comp and settings.board[2][0] == settings.comp and settings.board[1][1] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "1,1"  
            print(f'The Computer chooses: {compChoice}')  
        elif settings.board[1][1] == settings.comp and settings.board[2][2] == settings.comp and settings.board[0][0] == " ":
            settings.board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][2] == settings.comp and settings.board[1][1] == settings.comp and settings.board[2][0] == " ":
            settings.board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][1] == settings.comp and settings.board[2][0] == settings.comp and settings.board[0][2] == " ":
            settings.board[0][2] = settings.comp
            compChoice = "0,2"
            print(f'The Computer chooses: {compChoice}') 
        elif settings.board[0][2] == settings.comp and settings.board[2][0] == settings.comp and settings.board[1][1] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "0,2"    
            print(f'The Computer chooses: {compChoice}') 

        elif settings.board[0][0] == settings.player1 and settings.board[0][1] == settings.player1 and settings.board[0][2] == " ":
            settings.board[0][2] = settings.comp
            compChoice = "0,2"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][1] == settings.player1 and settings.board[0][2] == settings.player1 and settings.board[0][0] == " ":
            settings.board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][0] == settings.player1 and settings.board[0][2] == settings.player1 and settings.board[0][1] == " ":
            settings.board[0][1] = settings.comp
            compChoice = "0,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][0] == settings.player1 and settings.board[1][1] == settings.player1 and settings.board[1][2] == " ":
            settings.board[1][2] = settings.comp
            compChoice = "1,2"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][1] == settings.player1 and settings.board[1][2] == settings.player1 and settings.board[1][0] == " ":
            settings.board[1][0] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][0] == settings.player1 and settings.board[1][2] == settings.player1 and settings.board[1][1] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[2][0] == settings.player1 and settings.board[2][1] == settings.player1 and settings.board[2][2] == " ":
            settings.board[2][2] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[2][1] == settings.player1 and settings.board[2][2] == settings.player1 and settings.board[2][0] == " ":
            settings.board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[2][0] == settings.player1 and settings.board[2][2] == settings.player1 and settings.board[2][1] == " ":
            settings.board[2][1] = settings.comp
            compChoice = "2,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][0] == settings.player1 and settings.board[1][0] == settings.player1 and settings.board[2][0] == " ":
            settings.board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][0] == settings.player1 and settings.board[2][0] == settings.player1 and settings.board[0][0] == " ":
            settings.board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][0] == settings.player1 and settings.board[2][0] == settings.player1 and settings.board[1][0] == " ":
            settings.board[1][0] = settings.comp
            compChoice = "1,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][1] == settings.player1 and settings.board[1][1] == settings.player1 and settings.board[2][1] == " ":
            settings.board[2][1] = settings.comp
            compChoice = "2,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][1] == settings.player1 and settings.board[2][1] == settings.player1 and settings.board[0][1] == " ":
            settings.board[0][1] = settings.comp
            compChoice = "0,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][1] == settings.player1 and settings.board[2][1] == settings.player1 and settings.board[1][1] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][2] == settings.player1 and settings.board[1][2] == settings.player1 and settings.board[2][2] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][2] == settings.player1 and settings.board[2][2] == settings.player1 and settings.board[0][2] == " ":
            settings.board[0][2] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][2] == settings.player1 and settings.board[2][2] == settings.player1 and settings.board[1][2] == " ":
            settings.board[1][2] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][2] == settings.player1 and settings.board[1][1] == settings.player1 and settings.board[2][0] == " ":
            settings.board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][0] == settings.player1 and settings.board[1][1] == settings.player1 and settings.board[2][2] == " ":
            settings.board[2][2] = settings.comp
            compChoice = "2,2"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][2] == settings.player1 and settings.board[2][0] == settings.player1 and settings.board[1][1] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "1,1"    
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][1] == settings.player1 and settings.board[2][2] == settings.player1 and settings.board[0][0] == " ":
            settings.board[0][0] = settings.comp
            compChoice = "0,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[0][2] == settings.player1 and settings.board[1][1] == settings.player1 and settings.board[2][0] == " ":
            settings.board[2][0] = settings.comp
            compChoice = "2,0"
            print(f'The Computer chooses: {compChoice}')
        elif settings.board[1][1] == settings.player1 and settings.board[2][0] == settings.player1 and settings.board[0][2] == " ":
            settings.board[0][2] = settings.comp
            compChoice = "0,2"
            print(f'The Computer chooses: {compChoice}') 
        elif settings.board[0][2] == settings.player1 and settings.board[2][0] == settings.player1 and settings.board[1][1] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')

        elif settings.board[1][1] == " ":
            settings.board[1][1] = settings.comp
            compChoice = "1,1"
            print(f'The Computer chooses: {compChoice}')

        elif settings.board[0][0] == " " or settings.board[0][2] == " " or settings.board[2][0] == " " or settings.board[2][2] == " ":
            corners = ["0,0","0,2","2,0","2,2"]
            compChoice = random.choice(corners)
            while settings.board[int(compChoice[0])][int(compChoice[2])] != " ":
                compChoice = random.choice(corners)
            settings.board[int(compChoice[0])][int(compChoice[2])] = settings.comp
            print(f'The Computer chooses: {compChoice}')
        
        else:
            compChoice = str(random.randint(0,2)) + "," + str(random.randint(0,2))
            while settings.board[int(compChoice[0])][int(compChoice[2])] != " ":
                compChoice = str(random.randint(0, 2)) + "," + str(random.randint(0,2))
            settings.board[int(compChoice[0])][int(compChoice[2])] = settings.comp
            print(f'The Computer chooses: {compChoice}')
    
    elif settings.mode == "easy" and res == 2 or res == 3 or res == 4 or settings.mode == "medium" and res == 1 or res == 2 or settings.mode == "hard" and res == 1:
        compChoice = str(random.randint(0,2)) + "," + str(random.randint(0,2))
        while settings.board[int(compChoice[0])][int(compChoice[2])] != " ":
            compChoice = str(random.randint(0, 2)) + "," + str(random.randint(0,2))
        settings.board[int(compChoice[0])][int(compChoice[2])] = settings.comp
        print(f'The Computer chooses: {compChoice}')