## UTILS ##
def read_file() -> list:
    data = []
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            data.append(line.strip())
    return data

## SOLUTIONS ##
def solution1():
    data = read_file()

    total = 0
    for game in data:
        game_split = game.split(": ")

        game_id = game_split[0].split(" ")[-1]
        games = game_split[1].split("; ")

        valid = True

        for game_cubes in games:
            cubes = game_cubes.split(", ")

            cube_valid = True
            for cube in cubes:
                num, label = cube.split(" ")

                if label == "red" and int(num) > 12: 
                    cube_valid = False
                    break
                elif label == "green" and int(num) > 13: 
                    cube_valid = False
                    break
                elif label == "blue" and int(num) > 14: 
                    cube_valid = False
                    break

            if not cube_valid:
                valid = False
                break
        
        if valid:
            total += int(game_id)

    return total

def solution2():
    data = read_file()

    total = 0
    for game in data:
        game_split = game.split(": ")

        game_dict = {"red": [], "green": [], "blue": []}

        for game_cubes in game_split[1].split("; "):
            cubes = game_cubes.split(", ")
            for cube in cubes:
                num, label = cube.split(" ")
                game_dict[label].append(int(num))

        total += max(game_dict["red"]) * max(game_dict["green"]) * max(game_dict["blue"])

    return total

## MAIN ##
if __name__ == "__main__":
    p1_solution = solution1()
    print(f"*** Solution #1 ***\nAnswer: {p1_solution}")

    p2_solution = solution2()
    print(f"\n*** Solution #2 ***\nAnswer: {p2_solution}")