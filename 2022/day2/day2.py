import timeit

def part1() -> tuple:
    """
        A: rock B: paper C: scissors
        X: rock Y: paper Z: scissors
        Points
            A/X: 1 B/Y: 2 C/Z: 3
            Loss: 0 Draw: 3 Won: 6
    """
    # start time
    start = timeit.default_timer()
    # opening file
    file = open("data.txt", "r")
    # variables
    your_score = 0
    rules = {
        "R": [1, "A", "X"],
        "P": [2, "B", "Y"],
        "S": [3, "C", "Z"]
    }
    # game
    for line in file.readlines():
        # read moves
        opponent_move, your_move = (line.strip()).split(" ")
        # translate move
        for play, rule in rules.items():
            if your_move in rule:
                your_move = play
            if opponent_move in rule:
                opponent_move = play
        # logic #
        # win
        if (your_move == "R" and opponent_move == "S") or (your_move == "P" and opponent_move == "R") or (your_move == "S" and opponent_move == "P"):
            your_score += rules[your_move][0] + 6
        # tie
        elif your_move == opponent_move:
            your_score += rules[your_move][0] + 3
        # loss
        else:
            your_score += rules[your_move][0]
    # end time
    stop = timeit.default_timer()
    # return
    return(your_score, stop-start)

def part2()  -> tuple:
    """
        A: rock B: paper C: scissors
        X: rock Y: paper Z: scissors
        Points
            A/X: 1 B/Y: 2 C/Z: 3
            Loss: 0 Draw: 3 Won: 6
        Extra
            X: Loss Y: Draw Z: Win
    """
    # start time
    start = timeit.default_timer()
    # opening file
    file = open("data.txt", "r")
    # variables
    your_score = 0
    rules = {
        "R": [1, "A"],
        "P": [2, "B"],
        "S": [3, "C"],
    }
    conditions = {
        "Win": {"R": "P", "P": "S", "S": "R"},
        "Lose": {"R": "S", "P": "R", "S": "P"}
    }
    # game
    for line in file.readlines():
        # read moves
        opponent_move, your_move = (line.strip()).split(" ")
        # translate move
        for play, rule in rules.items():
            if opponent_move in rule:
                opponent_move = play
        # logic #
        # win
        if your_move == "Z":
            move = conditions["Win"][opponent_move]
            your_score += rules[move][0] + 6
        # tie
        elif your_move == "Y":
            your_score += rules[opponent_move][0] + 3
        # loss
        else:
            move = conditions["Lose"][opponent_move]
            your_score += rules[move][0]
    # end time
    stop = timeit.default_timer()
    # return
    return(your_score, stop-start)

if __name__ == "__main__":
    # part 1
    score, elapsed_time = part1()
    print(f"Part 1\nScore:\t{score}\nTime:\t{elapsed_time}\n")
    # part 2
    score, elapsed_time = part2()
    print(f"Part 2\nScore:\t{score}\nTime:\t{elapsed_time}\n")