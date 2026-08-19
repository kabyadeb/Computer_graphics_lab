import turtle 
import time
import math 

screen=turtle.Screen()
screen.setup(1000,800)
screen.setworldcoordinates(-300,-200,1000,800)
t=turtle.Turtle()
t.pensize(4)

def draw(p,color):
    t.pencolor(color)
    t.penup()
    t.goto(p[0])
    t.down()
    for x in p[1:]:
        t.goto(x)
    t.goto(p[0])

def translation(x,y,tx,ty):
    return x+tx,y+ty

def rotaion(x,y,angle):
    a=math.radians(angle)
    nx=x*math.cos(a)-y*math.cos(a)
    ny=x*math.sin(a)+y*math.sin(a)
    return nx,ny
def scaling(x,y,sx,sy):
    return x*sx,y*sy

trinagle=[(-20,-30),(50,-50),(0,50)]
draw(trinagle,"Blue")

translation=[translation(x,y,200,0) for x,y in trinagle]
draw(translation,"Purple")

rotated=[rotaion(x,y,20) for x,y in translation]
draw(rotated,"Red")
scaled=[scaling(x,y,2,2) for x,y in rotated]
draw(scaled,"green")



screen.exitonclick()