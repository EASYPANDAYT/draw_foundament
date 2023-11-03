import turtle

def draw_foundation(width, high, color):
    turtle.fillcolor(color)

    turtle.begin_fill()

    turtle.forward (width)
    turtle.left(90)
    turtle.forward (high)
    turtle.left(90)
    turtle.forward (width)
    turtle.left(90)
    turtle.forward (high)
    turtle.left(90)

    turtle.end_fill()

draw_foundation(100, 100, "red")
draw_foundation(150, 150, "blue")

turtle.done()
#чтобы спрашивала где рисовать
#стены над фундаментом






#turtle.left(40)
#turtle.forward (40)
#turtle.left(40)
#turtle.forward (40)
#turtle.left(40)
#turtle.forward (40)
#turtle.left(40)
#turtle.forward (40)
#turtle.left(40)
#turtle.forward (40)
#turtle.left(40)
#turtle.forward (40)
#turtle.left(40)
#turtle.forward (40)
#turtle.left(40)
#turtle.left(40)
#turtle.forward (40)
#turtle.done()

