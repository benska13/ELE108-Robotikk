import math
import turtle
import random

# make a line
line = turtle.Turtle()
# (ax+by+c)=0
a = -1
b = -1
c = 0
line.setpos((((-b * -500) - c) / a), -500)
line.setpos((((-b * 500) - c) / a), 500)
# line done

maxTurnAngle = 10
step = 5
demp = 40.0

turtles = []

for x in range(10):
    turtles.append(turtle.Turtle())
    turtles[x].setpos(random.randrange(-740, 740), random.randrange(-600, 600))
    turtles[x].setheading(random.randrange(0, 360))
    turtles[x].clear()
    turtles[x].speed(10)


def follow_line(tut, a, b, c, maxTurnAngle, demp):
    # Distance to nearest point on line
    distance_line = round((a * tut.xcor() + b * tut.ycor() + c) / math.sqrt(a * a + b * b))
    # Calculate the lines angel. PROBLEM!? angel between -90 and 90 degrees !?!
    angle_line = round(math.degrees(math.atan(- a / b)))
    # Turns the turtle towards the line. Problem continues
    angle_corr = round(math.degrees(math.atan(distance_line / demp)))
    # Try to correct the problem
    if angle_line < 0:
        angle_corr = - angle_corr
    # Calculate the angel to turn
    angle_ = angle_line - round(tut.heading()) - angle_corr
    # Sets the angle between -180 and 180 degrees
    while -180 > angle_ or angle_ > 180:
        if angle_ < -180:
            angle_ = angle_ + 360
        elif angle_ > +180:
            angle_ = angle_ - 360

    # print('Ang_to_p:', round(angle_), ' A line: ', angle_line, '  Car.h: ', tut.heading(), '  Corr a: ',
    #       round(math.degrees(math.atan(distance_line / demp))), '  D line: ', distance_line)

    # Turn the turtle
    if - maxTurnAngle <= angle_ <= maxTurnAngle:
        tut.setheading(angle_ + tut.heading())
    elif angle_ < - maxTurnAngle:
        tut.setheading(tut.heading() - maxTurnAngle)
    elif angle_ > maxTurnAngle:
        tut.setheading(tut.heading() + maxTurnAngle)


# Runs trough the list
while True:
    for tut in turtles:
        follow_line(tut, a, b, c, maxTurnAngle, demp)
        tut.forward(step)
