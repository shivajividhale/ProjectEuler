__author__ = 'Shivaji'

primeArray={}
primeArray[0]=2
primeArray[1]=3

def checkPrime(x):
    if x%2 == 0:
        return False
    for i in range(2,int(x/2)):
        if x%i==0:
            return False
    return True

i=2
x=4
while(i<10001):
    result=checkPrime(x)
    if result == True:
        primeArray[i]=x
        i=i+1
    x=x+1
print(primeArray[10000])