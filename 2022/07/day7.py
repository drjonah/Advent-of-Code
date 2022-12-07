import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..', '..'))
from speed import timer_func
from prettyformatter import pprint

###############################################################

@timer_func
def star1() -> None:
    # variables
    greatest_dir_size = 0
    directory = {}
    is_ls = False
    levels = []
    location = {}
    # run #
    # fill directory
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            file = line.strip().split(' ')
            # switching to list mode
            if file[1] == 'ls':
                is_ls = True
                continue
            # switching to moving directory modes
            if file[1] == 'cd' and file[2] != '/':
                is_ls = False
                # going back a level
                if file[2] == '..':
                    level_size = levels[-1]['size']
                    del levels[-1]
                    # resetting location unless if is on the 0th level and adding directory sizes
                    if len(levels) > 0:
                        location = levels[-1]
                        levels[-1]['size'] += level_size
                    continue
                # updating the current directory
                location = directory[file[2]] if len(levels) == 0 else location[file[2]]
                levels.append(location)
            # action
            if is_ls:
                # if on 0th level
                # dir structure = [dir size, files]
                if len(levels) == 0:
                    if file[0] == 'dir':
                        directory[file[1]] = {'size': 0}
                    else:
                        directory[file[1]] = int(file[0])
                # else
                else:
                    if file[0] == 'dir':
                        levels[-1][file[1]] = {'size': 0}
                    else:
                        levels[-1][file[1]] = int(file[0])
                        # adding the new file size to directorys total
                        for level in levels:
                            level['size'] += int(file[0])      

        pprint(directory)

        for dir in directory.values():
            if type(dir) is dict:
                if dir['size'] < 100000 and dir['size'] > greatest_dir_size:
                        greatest_dir_size += dir['size']
                        
        print(f'Star 1: Greatest Dir Size is {greatest_dir_size}')


@timer_func
def star2() -> None:
    # star 2
    pass

if __name__ == "__main__":
    # star 1
    star1()
    # star 2
    star2()