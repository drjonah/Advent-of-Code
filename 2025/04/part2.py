with open("input.txt") as file:
    f = file.readlines()
    cleaned = [ff.strip() for ff in f]

sc = [list(clean) for clean in cleaned]

def get_neighbors(grid, i, j):
    gl = len(grid)
    rl = len(grid[i])
    
    dir = [
        (-1, -1), (-1, 0), (-1, 1),
        (0,  -1),          (0, 1),
        (1,  -1), (1,  0), (1, 1)
    ]
    
    neighbors = []
    
    for dir_i, dir_j in dir:
        new_dir_i = dir_i + i
        new_dir_j = dir_j + j
        
        if (new_dir_i >= 0 and new_dir_i < gl) and (new_dir_j >= 0 and new_dir_j < rl):
            neighbors.append(grid[new_dir_i][new_dir_j])
            
    return neighbors


def filter_grid(grid: list):
            
    total = 0

    for i in range(len(sc)):
        for j in range(len(sc[i])):
            if sc[i][j] != "@":
                continue
            
            neighbors = get_neighbors(sc, i, j)
            if neighbors.count("@") < 4:
                total += 1
                grid[i][j] = "."
                
    return grid, total
            
grand_total = 0

while True:
    
    new_sc, total = filter_grid(sc)
    
    if total < 1:
        break
    
    sc = new_sc
    grand_total += total

            
print(f"Part 2: {grand_total}")
