# making bc last one was way too slow

# begin by generating list of truncable primes
def buildTruncList(num,numList,ansList):
    if len(ansList) < 11:
        for smallNum in [1,3,5,7,9]: #obviously a prime must be odd
            num += smallNum
            if isPrime(int(num)):
                buildTruncList(num)

