import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..', '..'))
from speed import timer_func

###############################################################

@timer_func
def star1():
    # variables
    contained = 0
    # run
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            # seperating the left and right
            one, two = line.strip().split(',')
            # converts the range to the range
            one = one.split('-')
            two = two.split('-')
            # fill sets with specified range
            one = set(range(int(one[0]), int(one[1])+1))
            two = set(range(int(two[0]), int(two[1])+1))
            # check if left is subset or superset of right
            if (one.issubset(two) or one.issuperset(two)):
                contained += 1
    # output
    print(f'Star 1: {contained} contained')

@timer_func
def star2():
    # variables
    contained = 0
    # run
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            # seperating the left and right
            one, two = line.strip().split(',')
            # converts the range to the range
            one = one.split('-')
            two = two.split('-')
            # fill sets with specified range
            one = set(range(int(one[0]), int(one[1])+1))
            two = set(range(int(two[0]), int(two[1])+1))
            # check if left is subset or superset of right or contains any similar element
            if (one.issubset(two) or one.issuperset(two) or len(one.intersection(two))>0):
                contained += 1
    # output
    print(f'Star 2: {contained} contained')

if __name__ == "__main__":
    # star 1
    star1()
    # star 2
    star2()