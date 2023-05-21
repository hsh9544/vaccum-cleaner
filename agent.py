import random


class Agent:
    '''
    simple reflex agent
    cleans if dirty
    takes random move if not dirty
    '''
    moves = ['up', 'down', 'left', 'right']
    actions = ['clean']

    def __init__(self) -> None:
        self.performance = 0

    def choose_action(self, percept):
        if percept == 'dirty':
            return 'clean'
        else:
            return random.choice(self.moves)

    def increase_performance(self):
        self.performance += 1
