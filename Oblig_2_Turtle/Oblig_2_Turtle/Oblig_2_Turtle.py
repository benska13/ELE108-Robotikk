import turtle


car = turtle.Turtle()
point = turtle.Turtle()
maxTurnAngle = 1

car.setpos(00, 00)
point.setpos(100, 200)

car.speed(1)
car.left(0)
car.clear()
point.clear()

while car.distance(point) > 10:

    angle_ = car.towards(point) - car.heading()
    print('Angle to point: ', angle_, ' Car a: ', car.heading(), ' Car to p: ', car.towards(point))

    if -360 <= angle_ < -180 or 0 < angle_ < 180:
        if 0 < angle_ < maxTurnAngle:
            car.left(angle_)
        else:
            car.left(maxTurnAngle)

    elif -180 <= angle_ < 0 or 180 <= angle_ < 360:
        if 0 > angle_ > - maxTurnAngle:
            car.right(-angle_)
        else:
            car.right(maxTurnAngle)

    car.forward(1)
