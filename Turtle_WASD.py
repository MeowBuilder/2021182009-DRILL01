import turtle

turtle.shape("turtle")

def Left():
    turtle.setheading(180)
    turtle.fd(50)
    turtle.stamp()
def Right():
    turtle.setheading(0)
    turtle.fd(50)
    turtle.stamp()
def Up():
    turtle.setheading(90)
    turtle.fd(50)
    turtle.stamp()
def Down():
    turtle.setheading(-90)
    turtle.fd(50)
    turtle.stamp()
def Reset():
    turtle.reset()


turtle.onkey(Up,'w')
turtle.onkey(Left,'a')
turtle.onkey(Down,'s')
turtle.onkey(Right,'d')
turtle.onkey(Reset,'Escape')
turtle.listen()

turtle.exitonclick()