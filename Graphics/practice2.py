from graphics import *
def main():
#Create a window of 500x500 pixels
    win = GraphWin("My Circle", 500, 500)
# Make the window scaled
# bottom leftmost corner is (0,0)
# top rightmost corner is (10,10)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
#Draw a circle centered around
    circle = Circle(Point(5,5),5)
    circle.setFill('red')
    circle.draw(win)
#Wait until mouse click in the window
    win.getMouse()
#Close Window
    win.close()
main()
