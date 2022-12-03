import timeit

LETTERS = list("abcdefghijklmnopqrstuvwxyz")

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
    # variables
    total_score = 0
    # run
    for rucksack in data:
        # runsack length
        rucksack_length = int(len(rucksack)/2)
        # splits runsack in half and converts them to lists
        rucksack_left, rucksack_right = list(rucksack[:rucksack_length]), list( rucksack[rucksack_length:])  
        # finds common letter and adds its worth  
        for letter in rucksack_left:
            if letter in rucksack_right:
                total_score += (LETTERS.index(letter.lower())+1)+26 if letter.isupper() else (LETTERS.index(letter.lower())+1)
                break
    # end time
    stop = timeit.default_timer()
    return(total_score, stop-start)

def part2(data: list) -> tuple:
    # start time
    start = timeit.default_timer()
    # variables
    total_score = 0
    # run
    for i in range(len(data)):
        # if multiple of 3
        if i%3 == 0:
            # grabbing rucksacks and converting to list
            rucksack1, rucksack2, rucksack3 = list(data[i]), list(data[i+1]), list(data[i+2])
            # finds common letter and adds its worth
            for letter in rucksack1:
                if letter in rucksack2 and letter in rucksack3:
                    total_score += (LETTERS.index(letter.lower())+1)+26 if letter.isupper() else (LETTERS.index(letter.lower())+1)        
                    break
    # end time
    stop = timeit.default_timer()
    return(total_score, stop-start)

if __name__ == "__main__":
    # list of elements in data.txt
    data = load_data()
    # part 1
    total_score, elapsed_time = part1(data)
    print(f"Part 1\nScore:\t{total_score}\nTime:\t{elapsed_time}")
    # part 2
    total_score, elapsed_time =part2(data)
    print(f"Part 2\nScore:\t{total_score}\nTime:\t{elapsed_time}")