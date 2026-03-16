## UTILS ##
def read_file() -> list:
    data = []
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            data.append(line.strip())
    return data

def get_neighbors(y_x: list, data: list, i: int, j: int) -> list:
    neighbors = [-1] * 8

    for location, quad in enumerate(y_x):
        y = quad[0] if (i > 0 and i < len(data)) else 0
        x = quad[1] if (j > 0 and j < len(data[i])) else 0

        neighbors[location] = data[i+y][j+x]

    return neighbors

def search_left(temp: str, row: str, x: int):
    if x < 0 or not row[x].isdigit():
        return temp
    
    return search_left(row[x] + temp, row, x - 1)

def search_right(temp: str, row: str, x: int):
    if x >= len(row) or not row[x].isdigit():
        return temp
    
    return search_right(temp + row[x], row, x + 1)

## SOLUTIONS ##
def solution1():
    data = read_file()

    total = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            character = data[i][j]
            # is symbol
            if (not character.isdigit() and character != "."):
                # get neighbors
                # [NW, N, NE, W, E, SW, S, SE]
                y_x = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
                neighbors = get_neighbors(y_x, data, i, j)
                
                # print(neighbors[0:3])
                # print(neighbors[3:5])
                # print(neighbors[5:])

                # mods
                if ((neighbors[0].isdigit() and neighbors[1].isdigit()) or neighbors[2].isdigit() and neighbors[1].isdigit()):
                    del y_x[1]

                elif ((neighbors[5].isdigit() and neighbors[6].isdigit()) or neighbors[7].isdigit() and neighbors[6].isdigit()):
                    del y_x[6]

                # search neighbors
                for neighbor_y, neighbor_x in y_x:
                    # neighbor = neighbors[n]
                    # neighbor_y, neighbor_x = y_x[n]

                    row = data[i+neighbor_y]
                    start = j+neighbor_x

                    left = search_left("", row, start)[0:-1]
                    right = search_right("", row, start)

                    if (left != "" or right != ""):
                        num = left + right

                        total += int(num)

                        # print(num)

    return total
        
def solution2():
    pass

## MAIN ##
if __name__ == "__main__":
    p1_solution = solution1()
    print(f"*** Solution #1 ***\nAnswer: {p1_solution}")

    # p2_solution = solution2()
    # print(f"\n*** Solution #2 ***\nAnswer: {p2_solution}")