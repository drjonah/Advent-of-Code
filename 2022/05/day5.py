import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..', '..'))
from speed import timer_func

###############################################################

def convert_groups(groups: list) -> list:
    # new list
    new_group = []
    # create new group with stack labels
    for label in groups[-1]:
        if label != ' ':
            new_group.append([label])
    # removes stack labels
    del groups[-1]
    # adds stock to stack labels
    for i in range(1, len(groups)+1):
        # group starting from bottom of stack
        group = groups[-i]
        for index, stock in enumerate(group):
            # ensures stock
            if stock != ' ' and stock != '[' and stock != ']':
                new_group[index//4].append(stock)
    # return
    return(new_group)

def arrange_groups_9000(groups: list, amount: int, initial: int, ending: int) -> list:
    # grabs stacks
    initial_group = groups[initial-1]
    ending_group = groups[ending-1]
    # moves around boxes 
    for _ in range(amount):
        ending_group.append(initial_group.pop(-1))
    # return
    return groups

def arrange_groups_9001(groups: list, amount: int, initial: int, ending: int) -> list:
    # grabs stacks
    initial_group = groups[initial-1]
    ending_group = groups[ending-1]
    # moves around boxes 
    move_group = initial_group[-amount:]
    ending_group += move_group
    del initial_group[-amount:]
    # return
    return groups

def get_top(groups: list) -> str:
    # name for top stack
    top = ''
    # grabs the top of each stack and adds to string
    for stack in range(len(groups)):
        top += groups[stack][-1]
    # return
    return top

@timer_func
def star1() -> None:
    # variables
    groups = []
    # run
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            # load groups
            if line[0] != '\n' and line[0] != 'm':
                groups.append(list(line)[1:len(line)-2])
                continue
            # calc groups
            elif line[0] == '\n':
                groups = convert_groups(groups)
                continue
            # sort logic
            line = line.strip().split(' ')
            # removes words
            del line[0]
            del line[1]
            del line[2]
            # sorts the commands
            amount, initial, ending = line
            # arranges groups
            groups = arrange_groups_9000(groups, int(amount), int(initial), int(ending))
    top = get_top(groups)
    print(f'Star 1: {top}')

@timer_func
def star2() -> None:
    # variables
    groups = []
    # run
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            # load groups
            if line[0] != '\n' and line[0] != 'm':
                groups.append(list(line)[1:len(line)-2])
                continue
            # calc groups
            elif line[0] == '\n':
                groups = convert_groups(groups)
                continue
            # sort logic
            line = line.strip().split(' ')
            # removes words
            del line[0]
            del line[1]
            del line[2]
            # sorts the commands
            amount, initial, ending = line
            # arranges groups
            groups = arrange_groups_9001(groups, int(amount), int(initial), int(ending))
    top = get_top(groups)
    print(f'Star 2: {top}')

if __name__ == "__main__":
    # star 1
    star1()
    # star 2
    star2()