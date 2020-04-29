import turtle
my_turtle = turtle.Turtle()

for i in range(10):
    my_turtle.circle(50 + 10*i)
    my_turtle.circle(-50 - 10 * i)
    my_turtle.left(90)
    my_turtle.circle(50 + 10 * i)
    my_turtle.circle(-50 - 10 * i)

turtle.mainloop()
