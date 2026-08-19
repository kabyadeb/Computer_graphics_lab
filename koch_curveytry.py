# import turtle

# t = turtle.Turtle()
# t.speed(0)

# def koch(length, level):

#     if level == 0:
#         t.forward(length)

#     else:
#         length = length / 3

#         koch(length, level - 1)

#         t.left(60)
#         koch(length, level - 1)

#         t.right(120)
#         koch(length, level - 1)

#         t.left(60)
#         koch(length, level - 1)


# # Draw Koch Curve
# t.penup()
# t.goto(-300, 0)
# t.pendown()

# koch(600, 3)

# turtle.done()
import turtle
import time

screen = turtle.Screen()
screen.setup(1000,800)

t = turtle.Turtle()
t.speed(0)
t.pensize(4)
def koch_curve(t, length, depth):
    if depth==0:
        t.forward(length)
        return
    length = length/3
    koch_curve(t, length, depth-1)
    t.left(60)
    koch_curve(t, length, depth-1)
    t.right(120)
    koch_curve(t, length, depth-1)
    t.left(60)
    koch_curve(t, length, depth-1)

def snowflake(t, length, depth):
    for i in range(3):
        koch_curve(t, length, depth)
        t.right(120)
for i in range(4):
    t.clear()
    t.penup()
    t.goto(-150, 100)
    t.setheading(0)
    t.pendown()
    if i == 0:
        t.pencolor("purple")
    if i==1:
        t.pencolor("red")
    if i==2:
        t.pencolor("red")
    if i==3:
        t.pencolor("blue")
    if i==4:
        t.pencolor("purple")
    if i==5:
        t.pencolor("blue")
    else:
        t.pencolor("red")
    snowflake(t,300,i)
    screen.update()
    time.sleep(1)

screen.exitonclick()