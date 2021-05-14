import sys
import random
import requests



def row_string(row):
    return '  {} | {} | {}  \n'.format(row[0], row[1], row[2])

def board_string(places):
    return ' ---+---+--- \n'.join([row_string(places[(i * 3):(i * 3) + 3]) for i in range(3)]) + '\n'




def join_values(values):
    return '&'.join(['value={}'.format(value) for value in values])

def get_move(values):
    try:
        return int(requests.get('http://localhost:5000/random/choice?{}'.format(join_values(values))).json()['value'])
    except:
        return random.choice(values)




def legal_positions(places):
    return [i for i in range(len(places)) if places[i] == '.']

def make_move(places, position, player):
    return [player if i == position else places[i] for i in range(len(places))], next_player(player)




def next_player(player):
    return 'X' if player == 'O' else 'O'




def has_row(places, player):
    return any(places[(i * 3):(i * 3) + 3].count(player) == 3 for i in range(3))

def has_column(places, player):
    return any([places[i], places[i + 3], places[i + 6]].count(player) == 3 for i in range(3))

def has_diagonal(places, player):
    return [places[0], places[4], places[8]].count(player) == 3 or [places[2], places[4], places[6]].count(player) == 3




def board_win(places):
    return any([has_row(places, player) or has_column(places, player) or has_diagonal(places, player) for player in ['X', 'O']])

def board_full(places):
    return len([p for p in places if p == '.']) == 0

def game_over(places):
    return board_win(places) or board_full(places)





def main(argv):
    print('\nTic Tac Toe Simulator\n')

    board, player = ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 'X'

    while not game_over(board):
        try:
            board, player = make_move(board, get_move(legal_positions(board)), player)
            print(board_string(board))
        except:
            print('Unexpected error occcurred.')
            break



if __name__ == "__main__":
    main(sys.argv[1:])
