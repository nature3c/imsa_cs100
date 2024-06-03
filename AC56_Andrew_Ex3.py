#This code is all hand written but I looked at documentation cmath and math
#The methods I used were found on geeksforgeeks and w3Schools

import time
import cmath
import math

#start of 3.1
time.sleep(5) #program starts after 5 seconds

print("""Welcome to the Fizz Buzz game! Numbers divisble by 3 will
return Fizz and numbers divisble by 5 will return Buzz.
Numbersd divisble by both will return FizzBuzz. Every
output will print after 3 seconds. \n""")

for i in range(0,50): # for loop from 0 to 49

    if i % 3 == 0 and i %  5== 0: # divisible by 3 and 5 returns FizzBuzz check first to avoid printing Fizz or Buzz
        print("FizzBuzz", end=", ")
        time.sleep(3)
        
    elif i % 3 == 0: # anything divisible by 3 returns fizz
        print("Fizz", end=", ")
        time.sleep(3)
        
    elif i % 5 == 0: # divisible by 5 returns buzz
        print("Buzz", end=", ")
        time.sleep(3)
        
    else: #not divisible by 3 or 5 just print the number
        print(i, end=", ")
        time.sleep(3)
#end of 3.1"""


time.sleep(5)

#start of 3.2
on = True #set on to true so that the while loop repeats indefinately

while on == True:
    print("""\n \nWelcome to the quadratic equation solver! Please input the
coefficients (in decimal form) to the equation ax^2+bx+c""")

    num = input(str("Enter the 3 numbers separated by spaces: ")) # input number 
    string = any(i.isalpha() for i in num) # checks if there are numbers

    if string == True: # if there are numbers stop the program and tell its not numbers
        print("That is not a number \n")
        go = input("Would you like to continue? (y/n) ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            break
        
    else: # if input is a number assign those values into a, b, and c
        a,b,c = [float(n) for n in num.split(' ')]

    if a == 0: # if a = 0 then the equation is not quadratic and the solution is just -c
        print("This is not a quadratic equation \n")
        print("The solution is " + str(-abs(c)) + "\n")
        
        go = input("Would you like to continue? (y/n): ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            break
        
    elif a == 1 and b == 0: #solution is always 0 if a is 1 and b is 0 because vertex is on y axis
        print("The solution is 0 \n")
        
        go = input("Would you like to continue? (y/n): ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            print("That was not a choice. Script terminating...")
            break
    
    else: # if a is a nonzero or 1 value then just assign a to a to continue the program
        a = a

    determinant = math.pow(b, 2) - (4*a*c) #find the determinant
    
    if determinant == 0 or determinant > 0: #if determinant is positive then use regular math to find answers
        ans1 = (-abs(b) + math.sqrt(math.pow(b, 2) - (4*a*c)))/(2*a) #quadratic equation for positive answer
        ans2 = (-abs(b) - math.sqrt(math.pow(b, 2) - (4*a*c)))/(2*a) #quadratic equation for negative answer

        rounded_ans1 = float(round(ans1, 2)) #rounded to nearest hundreths
        rounded_ans2 = float(round(ans2, 2))

        print(print(str(a) + "x^2 + " + str(b) + "x + " + str(c) + " has 2 real solutions")) #print the solutions
        print("The solutions are: " + str(rounded_ans1) + " and " + str(rounded_ans2))
        print("\n")

        go = input("Would you like to continue? (y/n): ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            print("That was not a choice. Script terminating...")
            break
        
    elif determinant < 0: #if determinant is negative then use complex math
        ans1 = (-abs(b) + cmath.sqrt(math.pow(b, 2) - (4*a*c)))/(2*a)#quadratic equation for positive complex answer
        ans2 = (-abs(b) - cmath.sqrt(math.pow(b, 2) - (4*a*c)))/(2*a)#quadratic equation for negative complex answer

        rounded_ans1 = complex(round(ans1.real, 2), round(ans1.imag, 2)) #rounded to nearest hundreths
        rounded_ans2 = complex(round(ans2.real, 2), round(ans2.imag, 2))

        print(str(a) + "x^2 + " + str(b) + "x + " + str(c) + " has 2 imaginary solutions") #print complex solutions
        print("The solutions are: " + str(rounded_ans1) + " and " + str(rounded_ans2))
        print("\n")

        go = input("Would you like to continue? (y/n): ") #ask if user wants to continue
        if go == "y":
            continue
        elif go == "n": #kills script if they type n
            break
        else: #breaks if input is not y or n
            print("That was not a choice. Script terminating...")
            break
    

    

