import timeit

def part1():
    # start time
    start = timeit.default_timer()
    # opening file
    file = open("data.txt", "r")
    # declaring variables
    calories = []
    temp_calorie_count = 0
    # fill list
    for line in file.readlines():
        line = line.strip()

        if line != "":
            temp_calorie_count += int(line)
        else:
            calories.append(temp_calorie_count)
            temp_calorie_count = 0
    # end time
    stop = timeit.default_timer()
    # return
    return (max(calories), stop-start)

def part2():
    # start time
    start = timeit.default_timer()
    # opening file
    file = open("data.txt", "r")
    # declaring variables
    calories = []
    temp_calorie_count = 0
    # fill list
    for line in file.readlines():
        line = line.strip()

        if line != "":
            temp_calorie_count += int(line)
        else:
            calories.append(temp_calorie_count)
            temp_calorie_count = 0
    # get the top 3 from list
    first = max(calories)
    calories.remove(first)

    second = max(calories)
    calories.remove(second)

    third = max(calories)
    calories.remove(third)
    # end time
    stop = timeit.default_timer()
    # return
    return(first+second+third, stop-start)

if __name__ == "__main__":
    # part 1
    max_calorie, elapsed_time = part1()
    print(f"Method 1\nMax:\t{max_calorie}\nTime:\t{elapsed_time}\n")
    # part 2
    max_calorie, elapsed_time = part2()
    print(f"Method 2\nSum:\t{max_calorie}\nTime:\t{elapsed_time}\n")