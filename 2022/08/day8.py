import os
from pprint import pprint
import sys
sys.path.append(os.path.join(os.getcwd(), '..', '..'))
from speed import timer_func

###############################################################

def check_left(trees: list, tree_height: int, tree_index: int) -> tuple:
    # check the left
    total_left = 0
    left_trees = trees[0:tree_index]
    for tree in left_trees:
        total_left += 1
        if tree >= tree_height:
            return (False, total_left)
    return (True, total_left)

def check_right(trees: list, tree_height: int, tree_index: int) -> tuple:
    # check the right
    total_right = 0
    right_trees = trees[tree_index+1:]
    for tree in right_trees:
        total_right += 1
        if tree >= tree_height:
            return (False, total_right)
    return (True, total_right)
    

def check_top(trees: list, tree_height: int, tree_row_index: int, tree_index: int) -> tuple:
    # load top trees
    total_top = 0
    top = list()
    for i in range(len(trees)):
        if i == tree_row_index:
            break
        top.append(trees[i][tree_index])
    # check the top
    for tree in top:
        total_top += 1
        if tree >= tree_height:
            return (False, total_top)
    return (True, total_top)

def check_bottom(trees: list, tree_height: int, tree_row_index: int, tree_index: int) -> tuple:
    # load bottom trees
    total_bottom = 0
    bottom = list()
    for i in range(len(trees)):
        if i > tree_row_index:
            bottom.append(trees[i][tree_index])
    # check the top
    for tree in bottom:
        total_bottom += 1
        if tree >= tree_height:
            return (False, total_bottom)
    return (True, total_bottom)

@timer_func
def star1() -> None:
    # variables
    tree_map = list()
    visible_trees = 0
    # load trees
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            tree_map.append(list(line.strip()))
    # check trees
    for i, col in enumerate(tree_map):
        for j, row in enumerate(col):
            # if edge, it is visible
            if i == 0 or i == len(tree_map)-1 or j == 0 or j == len(col)-1:
                visible_trees += 1
            # check interior trees and if it is visible
            elif check_left(col, row, j)[0] or check_right(col, row, j)[0] or check_top(tree_map, row, i, j)[0] or check_bottom(tree_map, row, i, j)[0]:
                # print(col, row)
                visible_trees += 1
    print(f'Star 1: Visible Trees = {visible_trees}')

@timer_func
def star2() -> None:
    # star 2
    print('Will complete later...')

if __name__ == "__main__":
    # star 1
    star1()
    # star 2
    star2()