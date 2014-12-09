import random


class Agent:
    def get_action(self, available_actions):
        pass


class RandomAgent(Agent):
    def get_action(self, available_actions):
        random_action = random.choice(available_actions.keys())
        return available_actions[random_action]

class BestScoreAgent(Agent):
    def get_action(self, available_actions):
        best_move = sorted([(-score, move) for move, (board, score) in available_actions.iteritems()])[0][1]
        return available_actions[best_move]


class Human(Agent):
    def __init__(self):
        self.move_d = {'l': 'left', 'r': 'right', 'u': 'up', 'd': 'down'}

    def get_action(self, available_actions):
        while True:
            move = raw_input('Move: ')
            if move in self.move_d:
                move = self.move_d[move]
            if move in available_actions:
                return available_actions[move]