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
            
            if (int(row[column]) == 0): count0 += 1
            else: count1 += 1
            
        if (count0 > count1):
            gammaRate += '0'
            epsilonRate += '1'
        else: 
            gammaRate += '1'
            epsilonRate += '0'
    
    return int(gammaRate,2) * int(epsilonRate,2)
        

def partTwo(data: list()) -> int:
    
    pass

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
