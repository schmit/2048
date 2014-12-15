import time

from board import Board

class Game:
    def __init__(self, n, agent, verbose=False):
        ''' 
        initialize a game on an n by n board 

        the player is defined by agent, see agent.py
        '''
        self.n = n
        self.board = Board([[0 for _ in xrange(self.n)] for _ in xrange(self.n)])
        self.score = 0
        self.agent = agent
        self.verbose = verbose

        self.start_time = time.time()

        # fill board with two entries
        for _ in xrange(2):
            self.board.fill_random_entry()

    def play(self):
        '''
        play the game game
        '''
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
        '''
        updates board based on action, and adds new random number
        '''
        self.board = action[0]
        self.score += action[1]
        self.board.fill_random_entry()

    def get_play_time(self):
        '''
        return play time
        '''
        return time.time() - self.start_time

    def __repr__(self):
        return 'Score: {}\nBoard:\n{}'.format(self.score, self.board)

