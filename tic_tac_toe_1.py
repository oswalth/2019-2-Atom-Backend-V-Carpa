class TicTacToe():
    winner_conditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                         (1, 4, 7), (2, 5, 8), (3, 6, 9),
                         (1, 5, 9), (3, 5, 7))

    def __init__(self):
        # self.turns = turns
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.score = {
            1: [],
            -1: [],
        }
        self.player_flag = 1
        self.rounds = 0
        self.paint_board()
        # self.game()

    def turn(self, position):
        marker = 'X' if self.player_flag > 0 else 'O'
        # position = input('Enter position of a cell - ')

        if position.isdecimal():
            position = int(position)
            if 1 <= position <= 9:
                pass
            else:
                return('ValueError. Please, reenter position - ')
                return
        else:
            return('ValueError. Please, reenter position - ')
            return
        has_appeared = self.check_identity(position)
        if has_appeared:
            return has_appeared
        self.score[self.player_flag].append(position)
        position -= 1
        self.board[position // 3][position % 3] = marker
        self.player_flag *= -1
        self.paint_board()
        is_end = self.check()
        if is_end:
            return is_end

    def check_identity(self, position):
        for _, value in self.score.items():
            if position in value:
                return 'IdentityError. Please reenter position - '

    def paint_board(self):
        print('-' * 11)
        for i in range(3):
            print('|', end='')
            for j in range(3):
                print(self.board[i][j], end='  ')
            print('|\n')
        print('-' * 11)

    def reset(self):
        self.__init__()

    def check(self):
        msg = 'Congratulations to player number {}'
        for key, value in self.score.items():
            for condition in self.winner_conditions:
                if len(set(sorted(value)).intersection(condition)) == 3:
                    print(msg.format(key))
                    return msg.format(key)

    def game(self):
        i = 0
        while self.rounds <= 8:
            turn = input()
            res = self.turn(turn)
            if res == 'IdentityError. Please reenter position - ':
                print('IdentityError. Please reenter position - ')
                continue

            if res == 'ValueError. Please, reenter position - ':
                print('ValueError. Please, reenter position - ')
                continue
            self.rounds += 1

            if res:
                print(res)
                return res
        print('Draw')
        return('Draw')


tic_tac = TicTacToe()
tic_tac.game()
turns = ['1','2','5','3','9']
tic_tac = TicTacToe()
for turn in turns[:-1]:
    tic_tac.turn(turn)
tic_tac.turn(turns[-1])

"""
values = ['3', 's', '0', '-1', '2.5', 'TTTT', 'True', 'False']
expected = [None] + ['ValueError. Please, reenter position - '] * 7

for pair in zip(values, expected):
    tic_tac = TicTacToe()
    print(tic_tac.turn(pair[0]) == pair[1])"""
