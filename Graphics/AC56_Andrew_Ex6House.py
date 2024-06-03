import graphics

def main():
    win = graphics.GraphWin("House", 500, 500) #intialize the window
    win.setBackground("white")
    
    house(win) #call the draw house function

    message(win) #after drawing is done display the message
    
    win.getMouse()
    win.close()

def house(win):
    p1 = win.getMouse() #first click 1 corner of the house
    p2 = win.getMouse() #second click the opposite corner of house
    p3 = win.getMouse() #third click the center of the door
    p4 = win.getMouse() #fourth click the center of the window
    p5 = win.getMouse() #fifth click the apex of the roof
    
    house = graphics.Rectangle(p1, p2) #make the frame of the house with opposite endpoint clicks
    house.draw(win) #draw it
    
    door_width = (p2.getX() - p1.getX()) / 5 #1/5th the width of the frame
    door_height = p2.getY() - p3.getY() #from the top corner click subtract the 3rd door click to get the height of door
    
    door = graphics.Rectangle(graphics.Point(p3.getX() - door_width / 2, p1.getY()), #sets point to half the width of the door to the left and the y value of the bottom y of the house
                              graphics.Point(p3.getX() + door_width / 2, p3.getY())) #other positive half with the opposite corner at the height of the 3rd clicked point
    door.draw(win)
    
    window_size = door_width / 2 #because window is half the width of the door
    window = graphics.Rectangle(graphics.Point(p4.getX() - window_size / 2, p4.getY() - window_size / 2), #the left half of the window and down half
                                graphics.Point(p4.getX() + window_size / 2, p4.getY() + window_size / 2)) #right half of the window and up half
    window.draw(win)
    
    roof_height = p1.getY() - p5.getY() #height of the roof because p5 is the roof click 
    
    roof_start1 = graphics.Point(p1.getX(), p2.getY()) #bottom left click but with the height of second click to get the left corner 
    roof_start2 = graphics.Point(p2.getX(), p2.getY()) #top right corner click
    roof_peak = graphics.Point(p5.getX(), p1.getY() - roof_height) #x value of the click and y = the top of the house frame + the height of the roof
    
    # Draw roof
    roof = graphics.Polygon(roof_start1, roof_peak, roof_start2) #actually make the triangle
    roof.draw(win)
    
def message(win):
    text = graphics.Text(graphics.Point(win.getWidth() / 2, win.getHeight() - 20), "I hope you liked my house!!") #message at middle of the window
    text.setSize(12)                                                                                              #and 20 units above the bottom
    text.draw(win)

if __name__ == "__main__": #idiom to set the main function to the executed function
    main()
