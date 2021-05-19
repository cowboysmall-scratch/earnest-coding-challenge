import unittest

from game import tictactoe


class TestTicTacToe(unittest.TestCase):


    def test_join_values(self):
        values = [1, 2, 3]
        self.assertEqual(tictactoe.join_values(values), 'value=1&value=2&value=3')



    def test_row_string(self):
        row1    = ['.', '.', '.']
        string1 = '  . | . | .  \n'
        self.assertEqual(tictactoe.row_string(row1), string1)

        row2    = ['X', 'O', 'O']
        string2 = '  X | O | O  \n'
        self.assertEqual(tictactoe.row_string(row2), string2)



    def test_board_string(self):
        board1  = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        string1 = '  . | . | .  \n ---+---+--- \n  . | . | .  \n ---+---+--- \n  . | . | .  \n\n'
        self.assertEqual(tictactoe.board_string(board1), string1)

        board2  = ['X', '.', '.', '.', 'X', '.', '.', '.', 'X']
        string2 = '  X | . | .  \n ---+---+--- \n  . | X | .  \n ---+---+--- \n  . | . | X  \n\n'
        self.assertEqual(tictactoe.board_string(board2), string2)



    def test_legal_moves(self):
        board1     = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        positions1 = []
        self.assertEqual(tictactoe.legal_moves(board1), positions1)

        board2     = ['X', '.', '.', '.', 'X', '.', '.', '.', 'X']
        positions2 = [1, 2, 3, 5, 6, 7]
        self.assertEqual(tictactoe.legal_moves(board2), positions2)



    def test_make_move(self):
        board1 = ['X', 'X', 'X', 'X', '.', 'X', 'X', 'X', 'X']
        board2 = ['X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X']
        self.assertEqual(tictactoe.make_move(board1, 4, 'O'), board2)



    def test_has_row(self):
        board1 = ['X', 'X', 'X', '.', '.', '.', '.', '.', '.']
        self.assertTrue(tictactoe.has_row(board1, 'X'))
        self.assertFalse(tictactoe.has_row(board1, 'O'))

        board2 = ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
        self.assertTrue(tictactoe.has_row(board2, 'X'))
        self.assertFalse(tictactoe.has_row(board2, 'O'))

        board3 = ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X']
        self.assertTrue(tictactoe.has_row(board3, 'X'))
        self.assertFalse(tictactoe.has_row(board3, 'O'))



    def test_has_column(self):
        board1 = ['X', '.', '.', 'X', '.', '.', 'X', '.', '.']
        self.assertTrue(tictactoe.has_column(board1, 'X'))
        self.assertFalse(tictactoe.has_column(board1, 'O'))

        board2 = ['.', 'X', '.', '.', 'X', '.', '.', 'X', '.']
        self.assertTrue(tictactoe.has_column(board2, 'X'))
        self.assertFalse(tictactoe.has_column(board2, 'O'))

        board3 = ['.', '.', 'X', '.', '.', 'X', '.', '.', 'X']
        self.assertTrue(tictactoe.has_column(board3, 'X'))
        self.assertFalse(tictactoe.has_column(board3, 'O'))



    def test_has_diagonal(self):
        board1 = ['X', '.', '.', '.', 'X', '.', '.', '.', 'X']
        self.assertTrue(tictactoe.has_diagonal(board1, 'X'))
        self.assertFalse(tictactoe.has_diagonal(board1, 'O'))

        board2 = ['.', '.', 'X', '.', 'X', '.', 'X', '.', '.']
        self.assertTrue(tictactoe.has_diagonal(board2, 'X'))
        self.assertFalse(tictactoe.has_diagonal(board2, 'O'))



    def test_board_win(self):
        board1 = ['X', 'X', 'X', '.', '.', '.', '.', '.', '.']
        self.assertTrue(tictactoe.board_win(board1, 'X'))
        self.assertFalse(tictactoe.board_win(board1, 'O'))

        board2 = ['.', '.', 'X', '.', '.', 'X', '.', '.', 'X']
        self.assertTrue(tictactoe.board_win(board2, 'X'))
        self.assertFalse(tictactoe.board_win(board2, 'O'))

        board3 = ['X', '.', '.', '.', 'X', '.', '.', '.', 'X']
        self.assertTrue(tictactoe.board_win(board3, 'X'))
        self.assertFalse(tictactoe.board_win(board3, 'O'))

        board4 = ['.', 'O', '.', '.', 'X', '.', '.', 'O', '.']
        self.assertFalse(tictactoe.board_win(board4, 'X'))
        self.assertFalse(tictactoe.board_win(board4, 'O'))



    def test_board_full(self):
        board1 = ['X', 'O', 'X', 'X', 'O', 'O', 'X', 'O', 'X']
        self.assertTrue(tictactoe.board_full(board1))

        board2 = ['.', 'O', '.', '.', 'X', '.', '.', 'O', '.']
        self.assertFalse(tictactoe.board_full(board2))




if __name__ == '__main__':
    unittest.main()
