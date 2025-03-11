import turtle


turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(10)
turtle.colormode(255)
colors = ["red", "blue"]

def rgb_color(i):
    r = (i * 3) % 256
    g = (i * 5) % 256
    b = (i * 7) % 256
    return (r, g, b)

turtle.tracer(2, 10)

t.hideturtle()
for number in range(400):
    t.pencolor(rgb_color(number)) 
    t.forward(number + 1)
    t.pencolor(colors[number % 2])
    t.right(89)
    t.pensize(0.2)

turtle.update() 
turtle.done()