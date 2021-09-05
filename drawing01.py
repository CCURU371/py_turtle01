import turtle
import time

turtle.setup(600,600)
turtle.bgcolor(0,0,0)

turtle1 = turtle.Turtle()
turtle1.speed(0)
turtle1.up() 
turtle1.setpos(0,-100) 
time.sleep(5)
turtle1.pendown()
turtle1.pensize(0)
n=70
angle = -(360/n)
for i in range(n):
    turtle1.pencolor(((i/n),0,1-(i/n)))
    turtle1.fd(10)
    turtle1.rt(angle)
    turtle1.circle(30)



turtle2 = turtle.Turtle()
turtle2.speed(0)
turtle.up()
turtle2.setpos(0,-100)
turtle.down()
turtle2.pensize(0)
n=70
angle = -(360/n)
for i in range(n):
    turtle2.pencolor(((i/n),0,1-(i/n)))
    turtle2.fd(10)
    turtle2.rt(angle)
    turtle2.circle(60)



turtle3 = turtle.Turtle()
turtle3.speed(60)
turtle3.pensize(0)
n=70
angle = -(360/n)
for i in range(n):
    turtle2.pencolor(0,0,0)
    turtle2.fd(10)
    turtle2.rt(angle)
    turtle2.circle(60)



turtle4 = turtle.Turtle()
turtle4.speed(60)
turtle4.setpos(0,-100) 
turtle4.pensize(0)
n=70
angle = -360/n
for i in range(n):
    turtle4.pencolor(0,0,0)
    turtle4.fd(10)
    turtle4.rt(angle)
    turtle4.circle(30)

turtle.done()