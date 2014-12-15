import argparse

from game import Game
import agent

# parse arguments
parser = argparse.ArgumentParser(description='2048 Game')
parser.add_argument('agent', metavar='a', type=str, default='human',
    help='the agent that plays the game')
parser.add_argument('-v', '--verbose', action='store_true',
    help='verbose flag')
args = parser.parse_args()

if args.agent == 'human':
    player = agent.Human()
    verbose = True
elif args.agent == 'random':
    player = agent.RandomAgent()
elif args.agent == 'bestscore':
    player = agent.BestScoreAgent()

if args.verbose:
    verbose = True
else:
    verbose = False

# run game
game = Game(4, player, verbose=verbose)
game.play()
