import turtle

turtle.colormode(255)


def draw_ring(color, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(50)

turtle.speed(3)
turtle.width(10)

draw_ring((255, 192, 203), -120, 0)  # Pink
draw_ring((128, 0, 128), 0, 0)       # Purple
draw_ring((255, 0, 0), 120, 0)       # Red
draw_ring((230, 230, 250), -60, -50) # Lavender
draw_ring((128, 0, 0), 60, -50)      # Maroon


turtle.hideturtle()
turtle.done()
