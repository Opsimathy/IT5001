

def create_zero_matrix(r, c):
    output = []
    for _ in range(r):
        row = []
        for _ in range(c):
            row.append(0)
        output.append(row)
    return output


def print_ttt(game):
    for i in range(3):
        print(f'{game[i][0]}|{game[i][1]}|{game[i][2]}')
        if i != 2:
            print('-----')


piece = ['X', 'O']


def check_valid_move(game, inp):
    return True


def check_win(game):
    return True


def ttt_gameplay():
    game = create_zero_matrix(3, 3)
    for i in range(3):
        for j in range(3):
            game[i][j] = i*3+j+1
    player = 0

    print_ttt(game)
    for i in range(9):  # Anyhow play 9 times
        print()
        pos = int(input(f'Player {piece[player]} move:')) - 1
        game[pos//3][pos % 3] = piece[player]
        player = 1 - player
        print_ttt(game)


game1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
game2 = [['X', 2, 3], ['X', 5, 6], ['X', 8, 9]]
game3 = [['O', 2, 3], [4, 'O', 6], [7, 'O', 9]]
game4 = [['X', 2, 'X'], [4, 'O', 6], ['X', 'O', 'X']]
game5 = [['X', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', 'X']]

print(check_win(game1))
print(check_win(game2))
print(check_win(game3))
print(check_win(game4))
print(check_win(game5))
