import turtle
import time

screen=turtle.Screen()
screen.setup(1000,800)
screen.setworldcoordinates(-300,-400,500,400)
t=turtle.Turtle()
t.speed(1)

#clipping window 
xmin,ymin=-100,-100
xmax,ymax=300,300

#region code 
top=8
bottom =4
right =2
left =1
#code 
def code(x,y):
    c=0
    if y>ymax:
        c|=top
    if(y<ymin):
        c|=bottom
    if(x>xmax):
        c|=right
    if(x<xmin):
        c|=left
    return c
def line(x1,y1,x2,y2,color,size):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.pencolor(color)
    t.pensize(size)
    t.goto(x2,y2)

#cohen-sutherland
def cohen(x1,y1,x2,y2):
    c1=code(x1,y1)
    c2=code(x2,y2)
    while True:
        if c1==0 and c2==0:
            line(x1,y1,x2,y2,"blue",4)
            break
        elif c1 & c2:
            break
        else:
            #kun point bahire ache seta ber kora
            if c1!=0:
                c=c1
            else: c=c2
            #top
            if c & top:
                x=x1+(x2-x1)*(ymax-y1)/(y2-y1)
                y=ymax
            #bottom
            elif c & bottom:
                x=x1+(x2-x1)*(ymin-y1)/(y2-y1)
                y=ymin
            #right
            elif c & right :
                y=y1+(y2-y1)*(xmax-x1)/(x2-x1)
                x=xmax
            #left
            elif c & left:
                y=y1+(y2-y1)*(xmin-x1)/(x2-x1)
                x=xmin
            if c==c1:
                x1,y1=x,y
                c1=code(x1,y1)
            else:
                x2,y2=x,y
                c2=code(x2,y2)
#clipping window draw
line(xmin,ymin,xmax,ymin,"red",4)
line(xmax,ymin,xmax,ymax,"red",4)
line(xmax,ymax,xmin,ymax,"red",4)
line(xmin,ymax,xmin,ymin,"red",4)

# Original line
line(-200, 150, 400, 250, "red", 2)

# Clipped line
cohen(-200, 150, 400, 250)
turtle.done()

