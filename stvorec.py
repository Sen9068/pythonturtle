import turtle


turtle.tracer(0, 0)
turtle.speed(10)

def stvorec(i):
    for number in range(4):
        turtle.hideturtle()
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.pen()
        turtle.forward(20)
        turtle.right(90)
    return(stvorec)

stvorec(1)


def blank(i):
    turtle.bgcolor('black')
    turtle.forward(11)
    turtle.pencolor('white')
    turtle.forward(10)
    turtle.pencolor('black')
    turtle.forward(100)
    return(blank)

blank(1)

def kruh(i):
    for number in range(20):
        turtle.hideturtle()
        turtle.pencolor('red')
        turtle.bgcolor('black')
        turtle.pen
        turtle.forward(6.5)
        turtle.right(30)
    return(kruh)
kruh(1)

def trojuholnik(i):
    for number in range(30):
        turtle.hideturtle()
        turtle.pencolor('yellow')
        turtle.bgcolor('black')
        turtle.pen
        turtle.forward(200)
        turtle.right(220)
    return(trojuholnik)

trojuholnik(1)

turtle.done()