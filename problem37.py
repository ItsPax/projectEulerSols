import math
def breakNum(n):
    n = list(n)
    numList = []
    while len(n) >= 1:
        numList.append(str(n))
        n.remove(n[0])
    return numList

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]
        mergeSort(left)
        mergeSort(right)
        [i,j,k] = [0,0,0]
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                alist[k] = right[j]
                j += 1
            else:
                alist[k] = left[i]
                i += 1
            k += 1
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

# build a list of right truncatable primes
# build a list of left truncatable primes
# find the union of the list
# what's my upper bound? or can I create a function that recursively keeps increasing the bound, saving data?

def leftTruncPrimes(numList):
# gives left truncatable primes using whatever you've determined to be LTP
# numList is list of strings
# use strs instead of ints + radix 10 + list implementation
    newNums = []
    for num in numList:
        numList.remove(num)
        for str(odd) in range(1,10,2):
            if isPrime(int(odd+num)):
                newNums.append(odd+num)
    return newNums


def rightTruncPrimes(numList):
# gives left truncatable primes using whatever you've determined to be LTP
# numList is list of strings
# use strs instead of ints + radix 10 + list implementation
    newNums = []
    for num in numList:
        numList.remove(num)
        for str(odd) in range(1,10,2): # have to str(rng)
            if isPrime(int(num+odd)):
                newNums.append(odd+num)
    return newNums

def isPrime(n):
    # try greedy solution as opposed to flex SoA
    for num in range(2,int(math.sqrt(n)+1)):
        if n%num == 0:
            return True
    return False

print(isPrime(17))


