import timeit

def load_data() -> list:
    # list to return
    data = []
    # open file
    with open("data.txt", "r") as FILE:
        for line in FILE.readlines():
            data.append(line.strip())
    # return
    return data

def part1(data: list) -> tuple:
    # start time
    start = timeit.default_timer()
    # end time
    stop = timeit.default_timer()

def part2(data: list) -> tuple:
    # start time
    start = timeit.default_timer()
    # end time
    stop = timeit.default_timer()

if __name__ == "__main__":
    # list of elements in data.txt
    data = load_data()
    # part 1
    part1(data)
    # part 2
    part2(data)