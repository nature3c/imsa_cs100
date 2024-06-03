#the raindrops code was taken from StackOverflow but I have made sure to understand every part of it

from graphics import *
import time
from random import randint, choice
from math import cos, sin, pi


WIDTH, HEIGHT = 800, 800

colorList = [
    color_rgb(255,255,255), #color codes for snow
    color_rgb(30,93,151),
]

def draw_snowman(win):
    bottom = Circle(Point(400, 600), 100)
    middle = Circle(Point(400, 450), 80)
    top = Circle(Point(400, 330), 60)
    
    bottom.setFill("white")
    middle.setFill("white")
    top.setFill("white")
    
    bottom.draw(win)
    middle.draw(win)
    top.draw(win)
    
    return bottom, middle, top

def draw_sun(win):

    sun = Circle(Point(700, 100), 50)
    sun.setFill("yellow")
    sun.draw(win)
    
    ray_length_factor = 2 #determine the length of the rays
    rays = []
    for angle in range(0, 360, 30): #rays every 30 degrees
        
        x2 = 700 + 50 * ray_length_factor * cos(angle * pi / 180) #end point of ray times the ray length factor
        y2 = 100 + 50 * ray_length_factor * sin(angle * pi / 180)
        ray = Line(Point(700, 100), Point(x2, y2))
        ray.setWidth(3)  #width of ray
        ray.setOutline("yellow")
        ray.draw(win)
        rays.append(ray)
    
    return sun, rays

def draw_snow(win):
    rects = [] #empty list called rects
    for _ in range(50): #_ to show that the value of the variable isn't going to be used
        for rect in list(rects):  #iterate over a shallow copy, a shallow copy is a copy of the list without the items inside
            rect.move(0, randint(10, 100)) #moves the rectangles down between 10 and 100 pixels

            #rect.getP1() gets the coordinate of the bottom left corner of the rectangle
            if rect.getP1().getY() > HEIGHT: #if the rectangle is greater than the height
                rect.undraw() #gets rid of rectangles underneath the window
                rects.remove(rect) #removes the rectangles from the list rect so that it doesn't affect rectangles that aren't visible

        x1 = randint(0, WIDTH - 5) #makes sure x coords of rectangle are inside the window (the rectangles are 5 pixels in width)
        y1 = randint(0, 10) #determines vertical position and makes sure it starts at top of window

        rect = Rectangle(Point(x1, y1), Point(x1 + 5, y1 + 20)) #creates rectangles based off of the constsnowts from above
        rect.setFill(choice(colorList)) #selects a color from the colorlist and colors the rectangle
        rect.draw(win) #draws the rectangle

        rects.append(rect) #adds the created rectangle to the list
    return rects #return rects to later clear it

def clear_snow(rects): #to clear the snow
    for rect in rects: #every element in rect
        rect.undraw() #clear everything

def melt_snowman(win, snowman_parts):
    for i in range(35):
        time.sleep(0.2) #to show that the snowman is melting
        for part in snowman_parts:
            part.undraw() #clear the snowman
        snowman_parts = [Circle(part.getCenter(), max(0, part.getRadius() - 3)) for part in snowman_parts] #make a new snowman w smaller radius
        for part in snowman_parts:
            part.setFill("white") 
            part.draw(win)

def main():
    win = GraphWin("5.3", WIDTH, HEIGHT)
    win.setBackground("light blue")
    
    snowman_parts = draw_snowman(win) #draw the snowman
    
    snow_rects = draw_snow(win) #start the snow animation

    clear_snow(snow_rects)#clear the snow after the snow animation stops
    
    sun = draw_sun(win) #draw the sun
    time.sleep(3)#wait 3 seconds
    
    melt_snowman(win, snowman_parts) #start melting snowman animation
    
    win.getMouse()
    win.close()

if __name__ == "__main__": #idiom in python to run the code without having a main method thats not a function, basically runs the cod
    main()
