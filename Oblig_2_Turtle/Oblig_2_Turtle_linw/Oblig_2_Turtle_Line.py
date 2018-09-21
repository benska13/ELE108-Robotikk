import math
import turtle
import random

# make a line
line = turtle.Turtle()
# (ax+by+c)=0
a = 1
b = -1
c = 0
for y in range(100):
    line.setpos((((-b * y) - c) / a), y)
# line done

maxTurnAngle = 10
step = 5
demp = 40.0

# car = turtle.Turtle()
# car.setpos(-100, 00)
# car.speed(0)
# car.right(180)
# car.clear()

turtles = []

for x in range(1):
    turtles.append(turtle.Turtle())
    turtles[x].setpos(random.randrange(-400, 400), random.randrange(-300, 300))
    turtles[x].setheading(random.randrange(0, 360))
    turtles[x].clear()
    turtles[x].speed(10)


def follow_line(tut, a, b, c, maxTurnAngle, demp):
    # Distance to line and nearest point on line
    distance_line = round((a * tut.xcor() + b * tut.ycor() + c) / math.sqrt(a * a + b * b))
    # line_x = ((b * (b * car.xcor() - a * car.ycor()) - a * c) / (a * a + b * b))
    # line_y = (a * (-b * car.xcor() + a * car.ycor()) - b * c) / (a * a + b * b)

    angle_line = round(math.degrees(math.atan(- a / b)))
    if angle_line < 0:
        angle_line = angle_line + 180
        distance_line = distance_line

    angle_ = angle_line - round(tut.heading()) - round(math.degrees(math.atan(distance_line / demp)))

    while -180 > angle_ or angle_ > 180:
        if angle_ < -180:
            angle_ = angle_ + 360
        elif angle_ > +180:
            angle_ = angle_ - 360

    print('Ang_to_p:', round(angle_), ' A line: ', angle_line, '  Car.h: ', tut.heading(), '  Corr a: ',
          round(math.degrees(math.atan(distance_line / demp))), '  D line: ', distance_line)

    if 0 < angle_ <= 180:
        if 0 < angle_ < maxTurnAngle:
            tut.left(angle_)
        else:
            tut.left(maxTurnAngle)
    elif -180 <= angle_ < 0:
        if 0 > angle_ > - maxTurnAngle:
            tut.right(-angle_)
        else:
            tut.right(maxTurnAngle)


while True:
    for tut in turtles:
        follow_line(tut, a, b, c, maxTurnAngle, demp)
        tut.forward(step)
