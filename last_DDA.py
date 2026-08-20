import turtle
import time
screen =turtle.Screen()
screen.setup(1000,800)
screen.setworldcoordinates(-300,-500,1000,800)
t=turtle.Turtle()
t.speed(1)

def axis():
    t.penup()
    t.goto(-300,0)
    t.pendown()
    t.color("black")
    t.pensize(1)
    t.goto(300,0)
    t.penup()
    t.goto(0,-300)
    t.pendown()
    t.color("black")
    t.goto(0,300)


def dda(x1,y1,x2,y2):
    dx=abs(x1-x2)
    dy=abs(x1-x2)
    steps=max(abs(dx),abs(dy))
    xin=dx/steps
    yin=dy/steps
    x=x1
    y=y1
    for i in range(steps+1):
        t.penup()
        t.goto(round(x),round(y))
        t.dot(4)
        time.sleep(.01)
        t.color("red")
        x=x+xin
        y=y+yin

axis()
dda(-50,50,200,-40)
turtle.done
screen.exitonclick()
