import random
import copy
import os


class Envirnoment:

    def __init__(self, env_size) -> None:
        self.env_size = env_size
        self.init_playground()
        self.init_visited()
        self.agent = None

    def init_playground(self):
        '''
        create 2D array with random dirty cells
        not perfectly random, just for test :)
        the solution is to give random weights to 0,1
        '''
        self.playground = []
        for i in range(self.env_size[0]):
            self.playground.append([random.choice((1, 0))
                                    for j in range(self.env_size[1])])

    def init_visited(self):
        '''
        create 2D array for storing cells visited by agent
        '''
        self.visited_cells = [
            [0 for j in range(self.env_size[1])] for i in range(self.env_size[0])]

    def random_selector(self):
        '''
        returns a random cell
        '''
        return (random.randrange(0, self.env_size[0]), random.randrange(0, self.env_size[1]))

    def add_agent(self, cleaner, location=None):
        self.init_agent_pos = location
        if location == None:
            self.init_agent_pos = self.random_selector()
        self.agent = [cleaner, self.init_agent_pos]

    def clean_cell(self, cell):
        i, j = cell
        self.playground[i][j] = 0

    def is_valid(self, cell):
        i, j = cell
        if (i < 0 or j < 0):
            return False
        try:
            _ = self.playground[i][j]
        except IndexError:
            return False
        return True

    def print_playground(self):
        CLEANER_CHAR = 'A'
        CLEANER_CHAR = '+'
        # CLEANER_CHAR = '\u2620'
        # CLEANER_CHAR = '\u058d'
        DIRT_CHAR = 'o'
        CLEAN_CHAR = ' '

        playground = copy.deepcopy(self.playground)
        if self.agent != None:
            i, j = self.agent[1]
            playground[i][j] = CLEANER_CHAR

        print('\u250f', (2*self.env_size[1]+1)*'\u2501', '\u2513', sep='')
        for i in range(self.env_size[0]):
            print('\u2503 ', end='')
            for j in range(self.env_size[1]):
                char = playground[i][j]
                if char == 0:
                    char = CLEAN_CHAR
                if char == 1:
                    char = DIRT_CHAR
                print(char, end=' ')
            print('\u2503')
        print('\u2517', (2*self.env_size[1]+1)*'\u2501', '\u251b', sep='')

    def update_visited(self, location):
        i, j = location
        self.visited_cells[i][j] = 1

    def is_done(self):
        for i in range(self.env_size[0]):
            for j in range(self.env_size[1]):
                if self.playground[i][j] == 1:
                    return False
        return True

    def run_episode(self):
        i, j = self.agent[1]
        if self.playground[i][j] == 1:
            percept = 'dirty'
        else:
            percept = 'clean'

        action = self.agent[0].choose_action(percept)
        success = self.take_action(action)
        self.update_visited(self.agent[1])
        return (action, success)

    def take_action(self, action):
        if action == 'clean':
            self.clean_cell(self.agent[1])
            self.agent[0].increase_performance()
            return 1

        elif action == 'up':
            i, j = -1, 0
        elif action == 'down':
            i, j = 1, 0
        elif action == 'right':
            i, j = 0, 1
        elif action == 'left':
            i, j = 0, -1

        new_location = (
            self.agent[1][0]+i,
            self.agent[1][1]+j
        )

        if self.is_valid(new_location):
            self.agent[1] = new_location
            return 1
        else:
            return 0


def test():
    room = Envirnoment((5, 10))
    agent = 'Miele'
    room.add_agent(agent)
    room.print_playground()


if __name__ == '__main__':
    test()
