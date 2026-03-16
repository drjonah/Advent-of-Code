

with open("./input.txt") as f:
    raw_data = f.readlines()
    clean_data = [d.strip() for d in raw_data]
    all_rotations = [(d[0], d[1:]) for d in clean_data]
    

directions = {
    "L": -1,
    "R": 1
}


def part1():
    crosses, running_combo = 0, 50

    for rotation in all_rotations:
        dir, distance = rotation
        mult = directions.get(dir)
        
        running_combo += (mult * int(distance)) 
        running_combo %= 100
        
        if running_combo == 0:
            crosses += 1 
            
    return crosses


def part2():
    crosses, running_combo = 0, 50

    for rotation in all_rotations:
        dir, distance = rotation
        dist_val = int(distance)
        
        prev = running_combo
        
        if dir == "R":
            target = prev + dist_val
            # End - start
            crosses += (target // 100) - (prev // 100)
        else: # "L"
            target = prev - dist_val
            # 100s crossed in interval [target, prev)
            crosses += ((prev - 1) // 100) - ((target - 1) // 100)

        running_combo = target % 100
            
    return crosses


part1_result = part1()
print(f"Part 1 result: {part1_result}")

part2_result = part2()
print(f"Part 2 result: {part2_result}")
