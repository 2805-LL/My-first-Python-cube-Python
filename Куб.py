import turtle

t = turtle.Turtle()
t.speed(5)

t.pendown()
for _ in range(4):
    t.forward(100)
    t.left(90)

t.left(45)

turtle.done()
