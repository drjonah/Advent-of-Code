from itertools import count
import time


def getData(fileName: str) -> list():
    data = list()

    with open(fileName, 'r') as FILE:
        for number in FILE.readlines():
            data.append(number)

    return data


def partOne(data: list()) -> int:

    gammaRate, epsilonRate = '', ''

    for column in range(len(data[0])-1):

        count0, count1 = 0, 0

        for row in data:

            if (int(row[column]) == 0):
                count0 += 1
            else:
                count1 += 1

        if (count0 > count1):
            gammaRate += '0'
            epsilonRate += '1'
        else:
            gammaRate += '1'
            epsilonRate += '0'

    return int(gammaRate, 2) * int(epsilonRate, 2)


def partTwo(data: list()) -> int:

    oxygenGenerator = data
    # oxygen generator rating
    for index in range(len(oxygenGenerator[0])-1):

        count0, count1 = list(), list()

        for row in oxygenGenerator:
            if (int(row[index]) == 0):
                count0.append(row)
            elif (int(row[index]) == 1):
                count1.append(row)

        if (len(count0) > len(count1)):
            oxygenGenerator = count0
        else:
            oxygenGenerator = count1

    co2Scrubber = data
    # CO2 scrubber rating
    for index in range(len(co2Scrubber[0])-1):

        count0, count1 = list(), list()

        if (len(co2Scrubber) == 1):
            break

        for row in co2Scrubber:
            if (int(row[index]) == 0):
                count0.append(row)
            elif (int(row[index]) == 1):
                count1.append(row)

        if (len(count0) > len(count1)):
            co2Scrubber = count1
        else:
            co2Scrubber = count0


    return int(oxygenGenerator[0], 2) * int(co2Scrubber[0], 2)


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
