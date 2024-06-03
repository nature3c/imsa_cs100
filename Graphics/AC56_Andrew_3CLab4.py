from graphics import *
import random

while True:
    win = GraphWin("Andrew 3C's Lab ", 800, 800) #initiate the window
    win.setBackground("light blue")


    def random_color(): #create a random color to fill the circles
        return color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_circles(point): #draw circles function with point as center
        for num_circles in circles_list: #makes the same number of circles as the number in circles_list
            radius = 125 #sets radius to 125, greater than 120 because radius reduces by 10 a max of 12 times
            for i in range(num_circles):
                circle = Circle(point, radius) #create circle at the click point and set radius = to 50
                circle.setFill(random_color()) #fill it with a random color
                circle.draw(win) #draw it
                radius -= 10 #subtract radius and repeat
    def message(win):
        text = Text(Point(win.getWidth() / 2, win.getHeight() - 20), "You drew " + num + " circles. Click anywhere to exit.") #message at middle of the window
        text.setSize(20) #sets text size to 20                                                                                  #and 20 units above the bottom
        text.draw(win) #draws it

    circles_list = [] #initiate empty list for every point that person clicks

    number_of_circles = 0 #need to define this before or else python gets mad that is not pointing to anything later in the program
    
    num = input("Enter the number of concentric circles 1-12 or q to stop: ")

    if num == "q":
        sys.exit(0)

    elif num.isalpha():
        print("Invalid input, please enter a number between 1 and 12 or q to stop.\n")
        win.close() #close the window because it doesn't do it automatically
        continue #rerun the program
        
    elif num.isdigit() and 1 <= int(num) <= 12: #number needs to be between 1 and 12, that many circles created
        circles_list.append(int(num)) #add that number into a list
        number_of_circles = int(num) #used later to make this many number of circles
        
    else:
        print("Invalid input, please enter a number between 1 and 12 or q to stop.\n")
        win.close()
        continue

    print("Please click on the graphical window to draw the circles.\n")

    #while True:
    for i in range(number_of_circles): #only the inputted number of circles are created
        point = win.getMouse() #the click point is stored in a variable called point
        draw_circles(point) #calls the draw circle function with point as an argument
    
    message(win) #after all the circles are drawn display the message
    
    if win.getMouse(): #after the person clicks to close the window
        win.close() 
        go = input("Would you like to continue? (y/n): ") #ask to rerun
        if go == "y":
            continue
        elif go == "n":
            break
        else:
            break


