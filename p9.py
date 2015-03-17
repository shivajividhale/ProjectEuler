__author__ = 'Shivaji'
import math
def checkIfTriplet(a,b):
    a1=a*a
    b1=b*b
    c=a1+b1
    result=math.sqrt(c)

    if result.is_integer()==False:

        return 0
    else:
        #print("Result of square root of a %d and b %d is %c",a,b,int(result))
        return result

class Triplets:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=int(c)
        self.sum=int(a+b+c)
        #if self.sum<1000:
            #print("Sum:",self.sum)
        self.str= "{0}{1}{2}".format(str(self.a), str(self.b), str(self.c))
        if self.sum==1000:
            print("Here!!!!!",a,b,c,a*b*c)

    def toString(self):

        return str

a=3
b=4
a1=5
Trips=[]
first=Triplets(3,4,5)
Trips.append(first)
while(a1<600):

    b1=a1+1

    while b1 < 600:
        result=checkIfTriplet(a1,b1)
        if result:
            x=Triplets(a1,b1,result)
            Trips.append(x)
            b1=b1+2
        else:
            b1=b1+2
    a1=a1+1
for x in Trips:
    print(x.a,x.b,x.c)
for x in Trips:
    #print("printing for",x.a,x.b,x.c)
    if x.b+x.a+x.c<1000:
        for y in range(2,50):
            j=Triplets(x.a*y,x.b*y,int(x.c)*y)
            #print(j.a,j.b,j.c)
            if j.sum==1000:
                print("Here:",j.a,j.b,j.c)


