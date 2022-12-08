import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..', '..'))
from speed import timer_func
from prettyformatter import pprint

###############################################################


@timer_func
def star1() -> None:
    # variables
    total = 0
    directory = {'./': 0}
    current_dir = './'
    # run #
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            file = line.strip().split(' ')
            # cd
            if file[1] == 'cd':
                # init
                if file[2] == '/':
                    continue
                # backwards 
                if file[2] == '..':
                    new_dir = ('/').join(current_dir.split('/')[:-2]) + '/'
                    directory[new_dir] += directory[current_dir]
                    current_dir = new_dir
                    continue
                # enters dir
                else:
                    current_dir += f'{file[2]}/'
                    continue
            # ls
            if file[1] == 'ls':
                continue
            # action
            if file[0] == 'dir':
                directory[current_dir + f'{file[1]}/'] = 0
            else:
                directory[current_dir] += int(file[0])
        # add file sizes
        for file_size in directory.values():
            if file_size < 100000:
                total += file_size
        print(f'Star 1: Greatest Dir Size is {total}')


@timer_func
def star2() -> None:
    # star 2
    pass

if __name__ == "__main__":
    # star 1
    star1()
    # star 2
    star2()