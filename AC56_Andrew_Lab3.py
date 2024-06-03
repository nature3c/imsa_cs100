import math

"""
ALGORITHM: 
Use a while loop to keep the program running until the user terminates it. Get an input, in descending order with 4 numbers separated by spaces.
Getting the numbers in descending order should make the program simpler and is not too much of a hassle for the user to do.
Check if theres any letters or zeros are in the input and if there is stop the program. Otherwise, assign the values a, b, c, and d where
a > b > c > d. Perimeter should be the same for all shapes so a + b + c + d. Area for square and rectangle should be the same where its a*c.
The diagonal, for squares and rectangles, should be the square root of a^2 + b^2. Using c will be explained later. If a = b = c = d then that
is a square so return that it is a square, the perimeter, area, and diagonal. Using c doesn't affect the square because all side lengths are
equal. For the rectangle case because there is always a pair that is longer than the other parallel pair a or b should be greater than c or d,
because the input is in descending order. The c makes sense because a long side and short side are next to eachother and form a triangle.
The hypotenuse of that triangle would be the diagonal. Area would be a*c so the two different length sides are accounted for.
For the trapezoid there are 2 different cases where the top base is longer or shorter than the 2 side lengths. If the top base is longer
then the statement would be a > b > c==d because b is the top longer base and c and d are the 2 side lengths that are equal. Those side lengths need
to be equal in order to create a trapezoid. Find the height using math and the area of a trapezoid is base * height. The math will be a bit
different if the top parallel side is shorter than the 2 non-parallel side lengths."""

on = True

while on == True:    
    print("\nWelcome to the 4 side shape checker!")
    
    sides = input(str("""Please input the 4 side lengths, in descending order,
separated by a space: """))
    string = any(i.isalpha() for i in sides) # checks if there are letters

    if string == True: # if there are letters stop the program and tell its not numbers
        print("ERROR: That is not a number \n")
        go = input("Would you like to continue? (y/n) ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            break
        
    else: # if input is a number assign those values into a, b, and c
        a,b,c,d = [float(n) for n in sides.split(' ')]


    if a >= b >= c >= d :
        print("Numbers are in descending order \n")
    else:
        print("ERROR: The numbers are not in descending order")
        go = input("Would you like to continue? (y/n) ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            break
        
    perimeter = float(a + b + c + d) #perimeter for all shapes
    rounded_perimeter = float(round(perimeter, 2)) #in case the perimeter is a long decimal
                              
    diagonal = float(math.sqrt(math.pow(a,2) + math.pow(c,2))) #diagonal for square and rectangle, chose a and c so it works for rectangle too
    rounded_diagonal = float(round(diagonal, 2))
                             
    area = a*c #area for square and rectangle, chose a and c so it works for rectangle too
    rounded_area = float(round(area,2)) # ^ rounded to 2 decimal places
    
    if a==0 or b==0 or c==0 or d==0: #zero case
        print("ERROR: This program cannot help you. Input sides to be non-zero. \n")
        go = input("Would you like to continue? (y/n) ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            break
        
    elif a == b == c == d: #sqaure case
        print("The shape is a SQUARE")
        print("The perimeter is: " + str(rounded_perimeter))
        print("The area is: " + str(rounded_area))
        print("The diagonal is: " + str(rounded_diagonal) + "\n")
        
        go = input("Would you like to continue? (y/n) ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            break
        
    elif a == b and c == d: #rectangle case
        print("The shape is a RECTANGLE")
        print("The perimeter is: " + str(rounded_perimeter))
        print("The area is: " + str(rounded_area))
        print("The diagonal is: " + str(rounded_diagonal) + "\n")
        
        go = input("Would you like to continue? (y/n) ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            break
        
    elif a > b > c == d: #trapezoid case where the top, parallel side is greater than the 2 non parallel sides
        leg = math.pow(((a-b)/2),2) #calculate the length of the leg and square it in order to put into pythagorean theorum
        height_squared = math.pow(c,2) - leg #find the hieght squared
        height = math.sqrt(height_squared) #pythagoreon theorum to find the height
        rounded_height = float(round(height, 2)) #round the height to 2 decimal places
        area2 = a*height #find the area which is base * height
        rounded_area2 = float(round(area2, 2)) #round the area
        
        print("The shape is a TRAPEZOID")
        print("The perimeter is: " + str(rounded_perimeter))
        print("The height is: " + str(rounded_height))
        print("The area is: " + str(rounded_area2) + "\n")
        
        go = input("Would you like to continue? (y/n) ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            break

    elif a > b==c > d: #trapezoid case where the top, parallel side is less than the 2 non parallel sides
        leg = math.pow(((a-d)/2),2) #calculate the length of the leg and square it in order to put into pythagorean theorum
        height_squared = math.pow(b,2) - leg #find the hieght squared
        height = math.sqrt(height_squared) #pythagoreon theorum to find the height
        rounded_height = float(round(height, 2)) #round the height to 2 decimal places
        area2 = a*height #find the area which is base * height
        rounded_area2 = float(round(area2, 2))
        
        print("The shape is a TRAPEZOID")
        print("The perimeter is: " + str(rounded_perimeter))
        print("The height is: " + str(rounded_height))
        print("The area is: " + str(rounded_area2) + "\n")
        
        go = input("Would you like to continue? (y/n) ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            break
        
    else: #any other input that cannot make a quad
        print("These side lengths do not make a valid Quadrilateral")
        go = input("Would you like to continue? (y/n) ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            break










        
        

        
