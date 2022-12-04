import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..', '..'))
from speed import timer_func

###############################################################

@timer_func
def star1():
    # star 1
    pass

@timer_func
def star2():
    # star 2
    pass

if __name__ == "__main__":
    # star 1
    star1()
    # star 2
    star2()