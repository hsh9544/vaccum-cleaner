from agent import *
from environment import *
from utils import *
import time


def main():
    cs()

    while 1:
        try:
            i, j = map(int, input(
                'What are the environment dimentions? (rows columns): ').strip().split())
            if i < 1 or j < 1:
                raise Exception
        except:
            print('Something went wrong. Press enter to try again.')
            input()
            # delete_last_lines(3)
            cs()
        else:
            # delete_last_lines(1)
            cs()
            break

    size = (i, j)

    while 1:
        try:
            agent_i, agent_j = map(int, input(
                'What is the initial location for the agent? (starts from 0, rows columns): ').strip().split())
            if agent_i >= i or agent_j >= j or i < 0 or j < 0:
                raise Exception
        except:
            print('Something went wrong. Press enter to try again.')
            input()
            # delete_last_lines(3)
            cs()
        else:
            # delete_last_lines(1)
            cs()
            break

    init_pos = (agent_i, agent_j)

    while 1:
        try:
            speed = int(input(
                'How fast you want the program to run? Enter a value in [0,100]: ').strip())
            if speed > 100 or speed < 0:
                raise Exception
        except:
            print('Something went wrong. Press enter to try again.')
            input()
            # delete_last_lines(3)
            cs()
        else:
            # delete_last_lines(1)
            cs()
            break

    speed = speed*0.6 + 40
    speed = 1-(speed/100)

    run(size, init_pos, speed)


def run(env_size=(10, 10), agent_pos=None, speed=0.1):
    room = Envirnoment(env_size)
    cleaner = Agent()
    room.add_agent(cleaner, agent_pos)

    room.print_playground()
    print(f'\n\n\nAgent Performance: 0000')
    time.sleep(3)

    counter = 0

    while 1:
        if room.is_done():
            break

        action, success = room.run_episode()
        counter += 1

        # delete_last_lines(env_size[0]+6)
        cs()
        room.print_playground()
        print(f'\nSTEP: {counter:<5d} | ACTION: {action:<5}')
        if action == 'clean':
            print('searching for dirt ... found some! cleaning ... DONE!')
            wait = 1
        elif not success:
            print('searching for dirt ... HIT THE WALL :(')
            wait = 0.2
        else:
            print('searching for dirt ...')
            wait = 0
        print(f'Agent Performance: {cleaner.performance}')

        time.sleep((1+4*wait)*speed)


if __name__ == '__main__':
    main()
