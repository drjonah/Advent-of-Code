import time


def getData(fileName: str) -> list():
    data = list()

    with open(fileName, 'r') as FILE:
        for number in FILE.readlines():
            data.append(int(number))

    return data


def partOne(data: list()) -> int:

    increment = 0
    storedNumber = data[0]

    for number in data:
        if number > storedNumber:
            increment += 1
        storedNumber = number

    return increment


def partTwo(data: list()) -> int:

    increment = 0
    storedNumbers = data[0:3]
    storedSum = sum(storedNumbers)

    for number in data[3:]:
        del storedNumbers[0]
        storedNumbers.append(number)
        newSum = sum(storedNumbers)

        if newSum > storedSum:
            increment += 1

        storedSum = newSum

    return increment


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
