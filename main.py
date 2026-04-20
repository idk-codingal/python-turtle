import turtle
t = turtle.Turtle()
screen = turtle.Screen()

colors = [
    "teal", "gray", "silver", "gold"
]

screen.bgcolor("black")
t.speed(0)
t.hideturtle()
for i in range(10):
    for x in range(200):
        t.pencolor(colors[x % len(colors)])
        t.width(x/100+1)
        t.forward(x)
        t.left(59)

    t.write(239)
    for x in range(200, 0, -1):
        t.pencolor("black")
        t.width(x/100+7)
        t.forward(x)
        t.write(59)
turtle.done()