import turtle
import time

screen=turtle.Screen()
screen.setup(1000,800)
screen.setworldcoordinates(0,0,1000,800)
t=turtle.Turtle()

def point_put(x,y):
    t.penup()
    t.goto(x,y)
    t.dot(4)

def brasen(x1,y1,x2,y2):
    dx=abs(x1-x2)
    dy=abs(y1-y2)
    sx=1 if x1<x2 else -1
    sy=1 if y1<y2 else -1
    if dx>dy :

        p=2*dy-dx
        while x1!=x2:
            point_put(x1,y1)
            if p>=0 :
                y1+=sy
                p -= 2*dx
            x2+=sx
            p+=2*dy
    else:
        p=2*dx-dy
        while y1!=y2:
            point_put(x1,y1)
            if p>=0:
                x1+=sx
                p-=2*dy
            y2+=dy
            p+=2*dx
    point_put(x2,y2)
brasen(100,200,800,900)
