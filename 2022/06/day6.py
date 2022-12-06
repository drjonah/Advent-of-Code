import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..', '..'))
from speed import timer_func

###############################################################

def marker_search(buffer: list, unique: int) -> int:
    # find first marker
    for index in range(len(buffer)-3):
        # find the first group where there is a set of 4 unique elements
        if len(set(buffer[index:index+unique])) == unique:
            return index + unique

@timer_func
def star1() -> None:
    # variables
    buffer = []
    unique = 4
    # run
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            buffer += list(line.strip())
    print(f'Star 1: Marker @ {marker_search(buffer, unique)}')

@timer_func
def star2() -> None:
    # variables
    buffer = []
    unique = 14
    # run
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            buffer += list(line.strip())
    print(f'Star 2: Marker @ {marker_search(buffer, unique)}')

if __name__ == "__main__":
    # star 1
    star1()
    # star 2
    star2()