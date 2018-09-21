import turtle
import random

# Point that objects go to
point = turtle.Turtle()
# Object:
maxTurnAngle = 8
step = 5

# Make a list of turtles with random poisson
turtles = []
for x in range(10):
    turtles.append(turtle.Turtle())
    turtles[x].setpos(random.randrange(-740, 740), random.randrange(-600, 600))
    turtles[x].setheading(random.randrange(0, 360))
    turtles[x].clear()
    turtles[x].speed(10)


# Function that turns a turtle
def go_to_point(tut, point, maxTurnAngle):
    # Angle between turtle and point
    angle_ = round(tut.towards(point)) - round(tut.heading())
    # Sets the angle between -180 and 180 degrees
    while -180 > angle_ or angle_ > 180:
        if angle_ < -180:
            angle_ = angle_ + 360
        elif angle_ > +180:
            angle_ = angle_ - 360

    # print('Angle to point: ', angle_, ' Car a: ', tut.heading(), ' Car to p: ', round(tut.towards(point)))

    # Turn the turtle
    if - maxTurnAngle <= angle_ <= maxTurnAngle:
        tut.setheading(angle_ + tut.heading())
    elif angle_ < - maxTurnAngle:
        tut.setheading(tut.heading() - maxTurnAngle)
    elif angle_ > maxTurnAngle:
        tut.setheading(tut.heading() + maxTurnAngle)


# runs trough the list
while True:
    for tut in turtles:
        if tut.distance(point) > 5:
            go_to_point(tut, point, maxTurnAngle)
            tut.forward(step)
