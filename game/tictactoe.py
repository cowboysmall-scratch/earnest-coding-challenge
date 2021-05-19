import sys
import random
import requests



def row_string(row):
    return '  {} | {} | {}  \n'.format(row[0], row[1], row[2])

def board_string(board):
    return '{}\n'.format(' ---+---+--- \n'.join([row_string(board[(i * 3):(i * 3) + 3]) for i in range(3)]))



def legal_moves(board):
    return [i for i in range(len(board)) if board[i] == '.']

def make_move(board, move, player):
    return [player if i == move else board[i] for i in range(len(board))]

def next(player):
    return 'X' if player == 'O' else 'O'



def has_row(board, player):
    return any(board[(i * 3):(i * 3) + 3].count(player) == 3 for i in range(3))

def has_column(board, player):
    return any([board[i], board[i + 3], board[i + 6]].count(player) == 3 for i in range(3))

def has_diagonal(board, player):
    return [board[0], board[4], board[8]].count(player) == 3 or [board[2], board[4], board[6]].count(player) == 3



def board_win(board, player):
    return has_row(board, player) or has_column(board, player) or has_diagonal(board, player)

def board_full(board):
    return len([p for p in board if p == '.']) == 0

def game_over(board):
    return board_win(board, 'X') or board_win(board, 'O') or board_full(board)



def get_move(board, player):
    try:
        return int(requests.get('http://localhost:5000/random/choice?{}'.format(join_values(legal_moves(board)))).json()['value'])
    except:
        return random.choice(legal_moves(board))

def join_values(values):
    return '&'.join(['value={}'.format(value) for value in values])



def main(argv):
    print('\nTic Tac Toe Simulator\n')
    print('\n{}\n'.format(board_string(range(1, 10))))

    board  = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    player = 'X'

    while not game_over(board):
        board  = make_move(board, get_move(board, player), player)
        player = next(player)

        print('\n{}\n'.format(board_string(board)))

    print('X wins\n\n' if board_win(board, 'X') else 'O wins\n\n' if board_win(board, 'O') else 'Draw\n\n')



if __name__ == "__main__":
    main(sys.argv[1:])
