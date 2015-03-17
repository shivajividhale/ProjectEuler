__author__ = 'Shivaji'

x=2520
def isDivisible(x):
    for j in range(2,21):
        if x%j !=0:
            return False
    return True

while(True):
    result=isDivisible(x)
    if result==False:
        x=x+20
    else:
        print(x)
        break
