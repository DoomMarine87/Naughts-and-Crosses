def display_board(game):
    string = "—" * 9 + "\n"
    counter = 0
    for i in range(len(game)):
        for j in game[i]:
            string += f'|{j}|'
            counter += 1
            if counter % 3 == 0:
                string += '\n' + '—' * 9 + '\n'
    return string