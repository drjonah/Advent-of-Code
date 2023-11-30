import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..', '..'))
from speed import timer_func

###############################################################

class Bridge():
    def __init__(self) -> None:
        self.bridge = []
        self.H_pos = [-1, 0] # last list, first pos
        self.T_pos = [-1, -1] # last list, first pos

    def create_bridge(self, size) -> None:
        for _ in range(size):
            self.bridge.append(list('*'*size))

    def edit_bridge(self) -> None:
        self.bridge[self.H_pos[0]][self.H_pos[1]] = 'H'
        self.bridge[self.T_pos[0]][self.T_pos[1]] = 'T'
    
    def print_bridge(self) -> None:
        for x in self.bridge:
            print((' ').join(x))

    def move(self, direction: str, distance: int) -> None:
        for _ in range(distance):
            if direction == 'R':
                self.H_pos[1] += 1
                self.T_pos[1] += 1
            elif direction == 'U':
                self.H_pos[0] += 1
                self.T_pos[0] += 1
        print(self.H_pos, self.T_pos)
        self.edit_bridge()
        self.print_bridge()

@timer_func
def star1() -> None:
    # star 1
    bridge = Bridge()
    bridge.create_bridge(10)
    # bridge.print_bridge()
    bridge.move('R', 4)
    bridge.move('U', 4)

@timer_func
def star2() -> None:
    # star 2
    pass

if __name__ == "__main__":
    # star 1
    star1()
    # star 2
    star2()