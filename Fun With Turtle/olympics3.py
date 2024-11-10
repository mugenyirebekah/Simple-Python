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


turtle.penup()
turtle.goto(0, 150)  
turtle.color("black")
turtle.write("Pink Olympics!", align="center", font=("Arial", 24, "bold"))


draw_ring((255, 192, 203), -120, 0) 
draw_ring((255, 92, 203), 0, 0)    
draw_ring((255, 200, 203), 120, 0)       
draw_ring((230, 192, 203), -60, -50) 
draw_ring((255, 19, 240), 60, -50)     


turtle.hideturtle()
turtle.done()
