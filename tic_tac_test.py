import unittest
from tic_tac_toe_1 import TicTacToe


class TestTicTacToe(unittest.TestCase):
    s = 'Congratulations to player number 1'

    def test_value(self):
        error_msg = 'ValueError. Please, reenter position - '
        tic_tac = TicTacToe()
        self.assertEqual(tic_tac.turn('3'), None)
        tic_tac.reset()
        self.assertEqual(tic_tac.turn('s'), error_msg)
        tic_tac.reset()
        self.assertEqual(tic_tac.turn('0'), error_msg)
        tic_tac.reset()
        self.assertEqual(tic_tac.turn('-1'), error_msg)
        tic_tac.reset()
        self.assertEqual(tic_tac.turn('2.5'), error_msg)
        tic_tac.reset()
        self.assertEqual(tic_tac.turn('TTTT'), error_msg)
        tic_tac.reset()
        self.assertEqual(tic_tac.turn('True'), error_msg)
        tic_tac.reset()
        self.assertEqual(tic_tac.turn('False'), error_msg)

    def test_identity(self):
        error_msg = 'IdentityError. Please reenter position - '
        tic_tac = TicTacToe()
        tic_tac.turn('1')
        self.assertEqual(tic_tac.turn('1'), error_msg)

    def test_winner_1(self):
        msg = 'Congratulations to player number {}'
        turns = ['1', '2', '5', '3', '9']
        tic_tac = TicTacToe()
        for turn in turns[:-1]:
            tic_tac.turn(turn)
        self.assertEqual(tic_tac.turn(turns[-1]), msg.format(1))

    def test_winner_2(self):
        msg = 'Congratulations to player number {}'
        turns = ['1', '2', '3', '5', '4', '8']
        tic_tac = TicTacToe()
        for turn in turns[:-1]:
            tic_tac.turn(turn)
        self.assertEqual(tic_tac.turn(turns[-1]), msg.format(-1))

    def test_multiple_errors(self):
        turns = ['1', '2', '4', '5', '4', '5', '4', '5', '5', '5', '7']
        msg = 'Congratulations to player number {}'
        tic_tac = TicTacToe()
        for turn in turns[:-1]:
            tic_tac.turn(turn)
        self.assertEqual(tic_tac.turn(turns[-1]), msg.format(1))


if __name__ == '__main__':
    unittest.main()
