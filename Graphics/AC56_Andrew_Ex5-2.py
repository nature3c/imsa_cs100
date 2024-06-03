from graphics import * #why does + go down and - go up for y???

def draw(window, center): #window to set parameters for the where the house is going to be, center to show the center of the house
    
    roof = Polygon(Point(center.getX() - 45, center.getY() - 25), #first point 50 units left from the center and 20 units above center
                   Point(center.getX() + 45, center.getY() - 25), #second point is 50 units right and 20 units above center
                   Point(center.getX(), center.getY() - 80)) #tip of the roof at center and 80 units up
    roof.setFill("red") #sets color to red
    roof.draw(window)
                     #first point                                   #second point
    house = Rectangle(Point(center.getX() - 40, center.getY() + 25), Point(center.getX() + 40, center.getY() - 25))
    house.setFill("lightblue")
    house.draw(window)

    door = Rectangle(Point(center.getX() - 10, center.getY() + 25), Point(center.getX() + 10, center.getY() - 15))
    door.setFill("brown")
    door.draw(window)

    left_window = Rectangle(Point(center.getX() - 35, center.getY() + 5), Point(center.getX() - 15, center.getY() - 15))
    left_window.setFill("white")
    left_window.draw(window)

    right_window = Rectangle(Point(center.getX() + 35, center.getY() + 5), Point(center.getX() + 15, center.getY() - 15))
    right_window.setFill("white")
    right_window.draw(window)

n = int(input("Enter the number of houses: ")) #get n number of houses

box = GraphWin("Click to draw a house", 500, 500)
box.setBackground("white")

message = Text(Point(250, 100), "Click anywhere to draw a house")
message.draw(box)

for i in range(n): #n is the max number of houses
    message.setText("Click to place house")
    click = box.getMouse() #set click to where the mouse was clicked
    draw(box, click) #call the draw function in the window win and click is the center

message.setText("Click anywhere to quit.") #after the program is done
box.getMouse() #wait for mouse click
box.close()#terminate
