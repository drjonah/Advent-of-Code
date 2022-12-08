import os
from pprint import pprint
import sys
sys.path.append(os.path.join(os.getcwd(), '..', '..'))
from speed import timer_func


###############################################################


@timer_func
def star1() -> None:
    # variables
    total = 0
    directory = {'./': 0}
    current_dir = './'
    # run #
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines()[1:]:
            file = line.strip().split(' ')
            # cd
            if file[1] == 'cd':
                # backwards 
                if file[2] == '..':
                    current_dir = ('/').join(current_dir.split('/')[:-2]) + '/'
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
                temp_dir = ''
                for file_dir in current_dir.split('/')[:-1]:
                    temp_dir += file_dir + '/'
                    directory[temp_dir] += int(file[0])
        # add file sizes
        for file_size in directory.values():
            if file_size <= 100000:
                total += file_size
        print(f'Star 1: Greatest Dir Size is {total}')


@timer_func
def star2() -> None:
    # variables
    total = 0
    directory = {'./': 0}
    current_dir = './'
    # run #
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines()[1:]:
            file = line.strip().split(' ')
            # cd
            if file[1] == 'cd':
                # backwards 
                if file[2] == '..':
                    current_dir = ('/').join(current_dir.split('/')[:-2]) + '/'
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
                temp_dir = ''
                for file_dir in current_dir.split('/')[:-1]:
                    temp_dir += file_dir + '/'
                    directory[temp_dir] += int(file[0])
        # add file sizes
        total_disk = 70000000
        required = 30000000
        available = total_disk - directory['./']
        for file_size in directory.values():
            if (available + file_size) >= required and file_size < total_disk:
                total = file_size
        print(f'Star 2: Greatest Dir Size is {total}')

if __name__ == "__main__":
    # star 1
    star1()
    # star 2
    star2()