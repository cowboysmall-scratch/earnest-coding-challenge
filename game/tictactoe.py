import sys
import random
import requests



def row_string(row):
    return '  {} | {} | {}  \n'.format(row[0], row[1], row[2])

def board_string(board):
    return ' ---+---+--- \n'.join([row_string(board[(i * 3):(i * 3) + 3]) for i in range(3)]) + '\n'




def join_values(values):
    return '&'.join(['value={}'.format(value) for value in values])

def get_move(values):
    try:
        return int(requests.get('http://localhost:5000/random/choice?{}'.format(join_values(values))).json()['value'])
    except:
        return random.choice(values)




def legal_positions(board):
    return [i for i in range(len(board)) if board[i] == '.']

def move(board, position, player):
    return [player if i == position else board[i] for i in range(len(board))], 'X' if player == 'O' else 'O'




def has_row(board, player):
    return any(board[(i * 3):(i * 3) + 3].count(player) == 3 for i in range(3))

def has_column(board, player):
    return any([board[i], board[i + 3], board[i + 6]].count(player) == 3 for i in range(3))

def has_diagonal(board, player):
    return [board[0], board[4], board[8]].count(player) == 3 or [board[2], board[4], board[6]].count(player) == 3




def board_win(board):
    return any([has_row(board, player) or has_column(board, player) or has_diagonal(board, player) for player in ['X', 'O']])

def board_full(board):
    return len([p for p in board if p == '.']) == 0

def game_over(board):
    return board_win(board) or board_full(board)




def game(board, player):
    return [(board, player)] + game(*move(board, get_move(legal_positions(board)), player)) if not game_over(board) else [(board, player)]




def main(argv):
    try:
        print('\nTic Tac Toe Simulator\n')
        print('\n'.join([board_string(state[0]) for state in game(['.', '.', '.', '.', '.', '.', '.', '.', '.'], 'X')[1:]]))
    except:
        print('Unexpected error occcurred.')



if __name__ == "__main__":
    main(sys.argv[1:])
