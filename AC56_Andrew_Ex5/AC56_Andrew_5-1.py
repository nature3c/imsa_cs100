from graphics import *

window = GraphWin("Click to draw a house", 500, 500)
window.setBackground("white")

roof = Polygon(Point(205, 225), #first point 50 units left from the center and 20 units above center
                   Point(295, 225), #second point is 50 units right and 20 units above center
                   Point(250, 170)) #tip of the roof at center and 80 units up
roof.setFill("red") #sets color to red
roof.draw(window)
                     #first point                                   #second point
house = Rectangle(Point(210, 275), Point(290, 225))
house.setFill("lightblue")
house.draw(window)

door = Rectangle(Point(240, 275), Point(260, 235))
door.setFill("brown")
door.draw(window)

left_window = Rectangle(Point(215, 255), Point(235, 235))
left_window.setFill("white")
left_window.draw(window)

right_window = Rectangle(Point(285, 255), Point(265, 235))
right_window.setFill("white")
right_window.draw(window)

message = Text(Point(250, 100), "Click anywhere to quit")
message.draw(window)
window.getMouse() #wait for mouse click
window.close()#terminate
