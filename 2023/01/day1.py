import re

## UTILS ##
def read_file() -> list:
    data = []
    with open('data.txt', 'r') as FILE:
        for line in FILE.readlines():
            data.append(line.strip())
    return data

## SOLUTIONS ##
def solution1():
    # file data
    data = read_file()
    
    total = 0
    for calibration_line in data:
        found = re.findall(r"[1-9]", calibration_line)
        total += (int(found[0]) * 10) + int(found[-1])

    return total


def solution2():
    # file data
    data = read_file()

    conversion = {"one": 1, "two": 2, "three": 3,
                  "four": 4, "five": 5, "six": 6,
                  "seven": 7, "eight": 8, "nine": 9}
    regex_pattern = r"one|two|three|four|five|six|seven|eight|nine|[1-9]"

    total = 0
    for calibration_line in data:
        found = re.findall(regex_pattern, calibration_line)
        first = int(found[0]) if found[0].isdigit() else conversion[found[0]]
        last = int(found[-1]) if found[-1].isdigit() else conversion[found[-1]]
        total += first * 10 + last

    return total

## MAIN ##
if __name__ == "__main__":
    p1_solution = solution1()
    print(f"*** Solution #1 ***\nAnswer: {p1_solution}")

    p2_solution = solution2()
    print(f"\n*** Solution #2 ***\nAnswer: {p2_solution}")