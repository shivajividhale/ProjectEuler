__author__ = 'Shivaji'

X=0
Y=0
destX=19
destY=19
routes=0

def right(x,y):
    x += 1
    if y==destY and x==destX or x==destX and y==destY:
        routes += 1
        print(routes)
        return
    down(x,y)
    if x!=19:
        right(x,y)

def down(x,y):
    y += 1
    if y==destY and x==destX or x==destX and y==destY:
        routes +=1
        return
    if y!=19:
        down(x,y)
    right(x,y)

right(0,0)
down(0,0)
print(routes)


