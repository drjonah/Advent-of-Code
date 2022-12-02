import time

def getData(fileName: str) -> list():
    data = list()

    with open(fileName, 'r') as FILE:
        for number in FILE.readlines():
            data.append(number)

    return data


def partOne(data: list()) -> int:

    horizontal = 0
    depth = 0
    
    for intruction in data:
        direction = intruction.split(' ')[0]
        movement = int(intruction.split(' ')[1])
        
        if (direction == 'up'): depth += movement
        elif (direction == 'down'): depth -= movement
        else: horizontal += movement
        
    return horizontal * depth
        

def partTwo(data: list()) -> int:

    horizontal = 0
    depth = 0
    aim = 0
    
    for intruction in data:
        direction = intruction.split(' ')[0]
        movement = int(intruction.split(' ')[1])
        
        if (direction == 'up'): aim -= movement
        elif (direction == 'down'): aim += movement
        else: 
            horizontal += movement
            depth += aim * movement
        
    return horizontal * depth


def main():

    data = getData('data.txt')
    start = time.time()

    print('Problem 1: %s' % partOne(data))
    print('Problem 2: %s' % partTwo(data))

    end = time.time()
    executionTime = end - start

    print('Execution time: %.9f' % executionTime)


if __name__ == '__main__':
    main()
