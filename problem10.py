__author__ = 'Shivaji'

def isPrime(n):
    print("Checking for",n)
    if n==1 or n%2==0:
        return False
    for x in range(3,int(n/2)):
        if n%x==0:
            return False
    return True
sum=17
number=4
n=3
while(n<2000000):
    if n%2==0 or n%3==0 or n%5==0 or n%7==0:
        n=n+1
        continue
    elif isPrime(n):
        sum=sum+n
    n=n+1

print("Sum is:",sum)
