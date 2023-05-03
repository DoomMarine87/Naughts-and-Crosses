import settings

def display_board():
    string = "—" * 9 + "\n"
    counter = 0
    for i in range(len(settings.board)):
        for j in settings.board[i]:
            string += f'|{j}|'
            counter += 1
            if counter % 3 == 0:
                string += '\n' + '—' * 9 + '\n'
    return string
