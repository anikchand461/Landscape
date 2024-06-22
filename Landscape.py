from turtle import *
import turtle

s = Screen()
s.colormode(255)
hideturtle()
speed('fast')

up()
goto(-200, 150)
seth(270)
down()
for _ in range(2):
    fd(300)
    lt(90)
    fd(400)
    lt(90)

up()
goto(-200,150)
pensize(3)

for i in range(1,75):
    down()
    seth(0)
    pencolor(0 + i * 3, 85 + i * 2, 255)
    fd(400)
    up()
    goto(-200,150-i*3)

up()
goto(-200,-72)
pensize(3)
for i in range(1,28):
    down()
    seth(0)
    pencolor(255-i*9,235-i*5,255)
    fd(400)
    up()
    goto(-200, -72 - i*3)

#sun
up()
goto(-65,20)
seth(-90)
fillcolor('yellow')
pencolor('yellow')
begin_fill()
down()
circle(65)
end_fill()

#bridge
up()
goto(-200,-75)
pencolor('black')
pensize(7)
down()
seth(30)
circle(-400,60)

up()
goto(-200,-67)
pensize(5)
down()
seth(30)
circle(-400,60)

#pillars
up()
goto(-100,-150)
pensize(8)
down()
seth(90)
fd(225)

up()
goto(100,-150)
pensize(8)
down()
seth(90)
fd(230)

#pillar base
up()
goto(-100,-150)
pensize(14)
down()
seth(90)
fd(20)

up()
goto(100,-150)
pensize(14)
down()
seth(90)
fd(20)

#pillar strings
up()
goto(-100, 75)
down()
pensize(2.5)
seth(-108)
circle(-300, 35)

up()
goto(-100,75)
down()
seth(-60)
circle(180,43)
seth(22)
circle(180,43)

up()
goto(100,77)
down()
seth(-72)
circle(300, 35)

#border
up()
goto(-205,155)
down()
seth(-90)
pensize(6)
pencolor('white')
for i in range(2):
    fd(310)
    lt(90)
    fd(410)
    lt(90)

up()
goto(-210,160)
down()
seth(-90)
pensize(5)
pencolor('black')
for i in range(2):
    fd(320)
    lt(90)
    fd(420)
    lt(90)

s.mainloop()
