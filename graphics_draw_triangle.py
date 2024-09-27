# Triangle!!!!
# Interactive graphics program to draw a triangle

from graphics import *

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    

    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()  # Wait for the first mouse click
    p1.draw(win)
    
    p2 = win.getMouse()  # Wait for the second mouse click
    p2.draw(win)
    
    p3 = win.getMouse()  # Wait for the third mouse click
    p3.draw(win)

    # Use Polygon object to draw the triangle 
    triangle = Polygon(p1, p2, p3) 
    triangle.setFill("peachpuff") 
    triangle.setOutline("cyan") 
    triangle.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()  # Wait for the final mouse click
    win.close()     # Close the window

# Ensure main is called when the script is run
if __name__ == "__main__":
    main()
