
from graphics import*

def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 20, 255))

    win.setBackground(color_rgb(0,0,0))
    pt = Point(250, 250)
    cir = Circle(pt, 50)
    cir.setFill(color_rgb(100, 255, 50))
    cir.draw(win)
    


    win.getMouse()
    win.close()

main()
