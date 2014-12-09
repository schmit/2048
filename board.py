import random

class Board:
    def __init__(self, board):
        self.board = board
        self.moves = ['left', 'right', 'up', 'down']
        self.n = len(board)

    def get_available_actions(self):
        available_actions = {}
        for move in self.moves:
            board, valid, score = self.move(move)
            if valid:
                available_actions[move] = (board, score)
        return available_actions

    def move(self, move):
        if move == 'left':
            board, valid, score = self.move_left()
        elif move == 'right':
            board, valid, score = self.move_right()
        elif move == 'up':
            board, valid, score = self.move_up()
        elif move == 'down':
            board, valid, score = self.move_down()
        return board, valid, score

    def move_left(self):
        new_board = self.copy()
        score = 0
        for row in xrange(self.n):
            # squish row
            left_entry = 0
            nonzeros = [x for x in new_board[row] if x != 0]
            while left_entry < len(nonzeros)-1:
                if nonzeros[left_entry] == nonzeros[left_entry+1]:
                    nonzeros[left_entry] += nonzeros.pop(left_entry+1)
                    score += nonzeros[left_entry]

                left_entry += 1

            # append zeros
            new_board[row] = nonzeros + [0 for _ in xrange(self.n - len(nonzeros))]

        return new_board, new_board.board != self.board, score

    def move_right(self):
        board, valid, score = self.flip().move_left()
        return board.flip(), valid, score

    def move_up(self):
        board, valid, score = self.transpose().move_left()
        return board.transpose(), valid, score

    def move_down(self):
        board, valid, score = self.transpose().move_right()
        return board.transpose(), valid, score

    def copy(self):
        return Board([[self[i][j] for j in xrange(self.n)] for i in xrange(self.n)])

    def flip(self):
        return Board([[self[i][self.n-j-1] for j in xrange(self.n)] for i in xrange(self.n)])

    def transpose(self):
        return Board([[self[j][i] for j in xrange(self.n)] for i in xrange(self.n)])

    def open_spaces(self):
        return [(i, j) for i in xrange(self.n) for j in xrange(self.n) if self.board[i][j] == 0]

    def fill_random_entry(self):
        '''
        Fill a random open entry with a 2 wp 0.9 or a 2 wp 0.4
        '''
        random_entry = random.choice(self.open_spaces())
        if random.random() < 0.1:
            value = 4
        else:
            value = 2
        self.board[random_entry[0]][random_entry[1]] = value

    def __getitem__(self, i):
        return self.board[i]

    def __setitem__(self, i, x):
        assert len(x) == self.n, 'Length of row does not match'
        self.board[i] = x

    def __len__(self):
        return self.n

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            return self.board == other.board

    def __repr__(self):
        return '\n'.join([' '.join(['{:5d}'.format(x) for x in self.board[row]]) for row in xrange(self.n)])


