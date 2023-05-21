import random
import sys
import os

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def delete_last_lines(n=1):
    '''
    not working in windows cmd
    '''
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def cs():
    clear_screen()

def make_random_list(elements, count):
    left = count
    result = []
    for element in elements:
        repeat = random.randint(0, left)
        print(left, repeat, element)
        for _ in range(repeat):
            result.append(element)
        left -= repeat
    
    for _ in range(left):
        result.append(elements[-1])

    random.shuffle(result)
    return result


# print(make_random_list([1, 2, 0], 20))
