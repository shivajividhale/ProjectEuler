__author__ = 'Shivaji'

def isPrime(value):
    a=1
    x=1
    if value % 2 == 0 or value == 1:
        return False

    for x in range(2,int(value/2)):
        if value % x == 0:
            return False
        else:
            x += 1
    else:
        return True

v=600851475143
highest=1
for x in range(2,int(600851475143/2)):
    if isPrime(x) and v%x == 0:
        highest=x
        print(highest)
        if x > 6857:
            print("reached "+repr(x))


print(highest)


