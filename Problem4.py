__author__ = 'Shivaji'


x=10000
y=999*999
def checkPallin(x):
    s=str(x)
    length=s.__len__()
    for i in range(0,length):
        if s[i]!=s[length-1-i]:
            return False
    return True

for x in range(100,1000):
    for y in range(100,1000):
        j=x*y
        if checkPallin(j)== True and j>900000:
            print(j)




