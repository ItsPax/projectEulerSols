import math
# build a list of right truncatable primes
# build a list of left truncatable primes
# find the union of the list
# what's my upper bound? or can I create a function that recursively keeps increasing the bound, saving data?

def isPrime(n):
# try greedy solution as opposed to flex SoA
    for num in range(2,int(math.sqrt(n)+1)):
        if n%num == 0:
            return False
    return True


def leftTruncPrimes(numList):
# gives left truncatable primes using whatever you've determined to be LTP, until impossible
# numList is list of strings
# use strs instead of ints + radix 10 + list implementation
    newNums = []
    for num in numList:
        strList = [str(x) for x in [1,2,3,5,7,9]]
        for odd in strList:
            if isPrime(int(odd+num)):
                newNums.append(odd+num)
    return newNums


def rightTruncPrimes(numList):
# gives right truncatable primes using whatever you've determined to be RTP, until impossible
# numList is list of strings
# use strs instead of ints + radix 10 + list implementation
    newNums = []
    for num in numList:
        strList = [str(x) for x in range(1,10,2)]
        for odd in strList:
            if isPrime(int(num+odd)):
                newNums.append(num+odd)
    return newNums

def genRTP():
    RTP = []
    newNums = ['2','3','5','7']
    while len(newNums) != 0:
        newNums = rightTruncPrimes(newNums)
        for num in newNums:
            RTP.append(num)
            print(num)
    return RTP

def genLTP():
    LTP = []
    newNums = ['2','3','5','7']
    while len(newNums) != 0:
        newNums = leftTruncPrimes(newNums)
        for num in newNums:
            LTP.append(num)
            print(num)
    return LTP

ltp = genLTP()
rtp = genRTP()
mySum = 0
truncDict = {}
for num in ltp:
    truncDict[num] = True
for num in rtp:
    if num in truncDict:
        mySum += int(num)

print(mySum)

