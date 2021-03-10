def getFibonacci(x):
    if x==0 or x==1:
        return 1
    else:
        return getFibonacci(x-2) + getFibonacci(x-1)

def getNumberDigits(x):
    if x<10 and x>=0:
        return 1
    else:
        return 1 + getNumberDigits(x//10)