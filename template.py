class TicTacToe():
    winner_conditions = ((1,2,3), (4,5,6), (7, 8, 9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
    def __init__(self):
        self.board = [[1,2,3], [4,5,6], [7,8,9]]
        self.score = {
            1: [],
            -1: [],
        }
        self.player_flag = 1
        self.rounds = 0
        self.paint_board()
        self.game()
        #self.game()

    def turn(self):
        marker = 'x' if self.player_flag > 0 else 'o'
        position = input('Enter position of a cell - ')

        if position.isdecimal():
            position = int(position)
            if 1 <= position <= 9:
                position -= 1
            else:
                print('Error. Player {}, please reenter position - ')
                return
        else:
            print('Error. Player {}, please reenter position - ')
            return

        self.board[position // 3][position % 3] = marker
        self.score[self.player_flag].append(position) 
        self.player_flag *= -1
        self.paint_board()
        is_end = self.check()
        if is_end:
            return True

    def paint_board(self):
        print('-' * 11)
        #board = [0] * 9

        """for key, value in self.board.items():
            for position in value:
                board[position] = key"""

        for i in range(3):
            print('|', end='')
            for j in range(3):
                print(self.board[i][j], end='  ')
            print('|\n')
        print('-' * 11)

    def check(self):

        for key, value in self.score.items():
            for condition in self.winner_conditions:
                if len(set(sorted(value)).intersection(condition)) == 3:
                    print('Congratulations to player number {}'.format(key))
                    return True
    
    def game(self):
        while self.rounds <= 9:
            res = self.turn()
            self.rounds += 1
            if res:
                break
        else:
            print('Draw')

game = TicTacToe([3,1,6,2,9,0,0,0,0,0])

