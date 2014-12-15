from board import Board

class Game:
    def __init__(self, n, agent, verbose=False):
        self.n = n
        self.board = Board([[0 for _ in xrange(self.n)] for _ in xrange(self.n)])
        self.score = 0
        self.agent = agent
        self.verbose = verbose

        # fill board with two entries
        for _ in xrange(2):
            self.board.fill_random_entry()

    def play(self):
        while True:
            if self.verbose: print self
            available_actions = self.board.get_available_actions()
            # if no available move, game is over
            if len(available_actions) == 0:
                print '--- Game over ---'
                print self
                return self.score

            action = self.agent.get_action(available_actions)
            self.update(action)

    def update(self, action):
        self.board = action[0]
        self.score += action[1]
        self.board.fill_random_entry()

    def __repr__(self):
        return 'Score: {}\nBoard:\n{}'.format(self.score, self.board)

