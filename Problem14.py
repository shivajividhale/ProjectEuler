__author__ = 'Shivaji'
import math
dict={1:4,2:2,4:3}
actDict={1:4,2:2,4:3}
import operator
def calculateTerm(n):

    if n in dict:
        #print(""+repr(n)+"Already there. returning", dict[n])
        return dict[n]
    if math.log2(n).is_integer()==True:
        dict[n]=int(math.log2(n))+1
        #if n<1000001:
         #   actDict[n]=dict[n]
        #elements++
        #print("found out for in log ",n)
        ##print(dict)
        return int(math.log2(n)+1)
    if n==2:
        return 2
    if n%2 == 0:
        #print("Entered n%2==0 for:",n)
        j=int(n/2)
        x=calculateTerm(int(j))
        ##print("found out for in n mod 0",j)
        dict[j]=int(x)
        #if j<1000001:
         #   actDict[j]=int(x)
        #elements=elements+1
        ##print(dict)
        return int(x+1)
    if n%2 == 1:
        #print("Entered n%2==1 for:",n)
        j=3*n+1
        x=calculateTerm(int(j))
        ##print("found out for  n mod 1 ",j)
        ##print(""+repr((n-1)/3)+"%2 == 1",x)
        dict[j]=int(x)
        #if j<1000001:
         #   actDict[j]=int(x)
        #elements=elements+1
        ##print(dict)
        ##print("returning result to n=",n,x)
        return int(x+1)
#x=calculateTerm(13)
##print(dict[13])
##print(x)

elements=3
for x in range(1,1000001):
    ##print("Entered for,",x)
    #if x in dict:
        #elements=elements+1
        #continue
    ##print("Will calculate for ",x)
    xi=calculateTerm(x)
    actDict[x]=xi
    #print("for"+repr(x)+":",xi)
    #elements=elements+1

print("Dict",len(dict))
#print(dict)
print("Act Dict",len(actDict))
#print(actDict)

maxm=0
index =0
for x in range(1,len(actDict)+1):

    if x in actDict and x < 1000001:
        if maxm < actDict[x]:
            maxm=actDict[x]
            index=x
##print(dict)
print (maxm)
print(index)
"""
class startingNumber:
    dict={2:1,4:2}
    def __init__(self,number):
        self.value=number
        self.terms=0
        #print("Entered for:",self.value)

    def calculateTerm(self,number):
        n=number
        if (dict[number]):
            return dict[number]
        if n==2:
            #print("In n==2 Entered for:",n)
            return 1
        if n%2==1:
            #print("In n%2==1 Entered for:",n)
            n=3*n+1
            self.terms=1+self.calculateTerm(n)
            dict[self.value]=self.terms
        else:
            #print("In n%2==0 Entered for:",n)
            n=n/2
            self.terms=1+self.calculateTerm(n)
            dict[self.value]=self.terms
        return

x=int(input("Enter starting number"))
Obj=startingNumber(x)
Obj.calculateTerm(x)
#print("Number of terms:",Obj.terms)
"""