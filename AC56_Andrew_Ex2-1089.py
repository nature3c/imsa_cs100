print("""Welcome to Magic Puzzle.
Please input a 3 digit number that decreases from left to right by 1.
An example would be 432. Any other number will not be accepted. \n """)

redo = True

while redo == True:
    
    num = str(input("Input a 3 digit number (enter stop to exit): "))
    string = any(c.isalpha() for c in num) #checks for characters

    if num == "stop": #type stop to stop the script
        break
    elif string == True: #restart loop if not stop or number
        print("That is not a number")
        continue
    elif string == False: # continue with the script if a number is types
        num = int(num)

    #code below here works
    
    x = num%10 #third digit found by using modulo 10
    y = int((num%100 - x)/10) #the second digit of the number by doing modulo 100 and minus the last digit
    z = round((num - num%100 - num%10)/100) #first digit of the number found by subtracting the num by the 2nd digit * 10 and the last digit and rounded        

    if x+1==y and x+2==z:
        reversed_num = x*100 + y*10 + z
        print("The reversed number is: " + str(reversed_num))

        # x = x, x+1 = y, x+2 = z
        #  x+2 x+1 x      have to carry over 1 from 2nd digit to 3rd digit to subtract and same for 1st digit and second digit
        #-   x x+1 x+2
        #=   1   9   8

        difference = int(((x+2)*100 + (x+1)*10 + x) - (100*(x) + 10*(x+1) + (x+2)))
        print("The difference is: "  + str(difference))

        a = difference%10 #same code to reverse as above
        b = int((difference%100 - x)/10)
        c = round((difference - difference%100 - difference%10)/100)

        reverse_difference = a*100 + b*10 + c
        
        print("The reverse of the difference is: " + str(reverse_difference))

        diff_sum = difference + reverse_difference
        print("198 + 891 = " + str(diff_sum))

        print("\n")
        
        again = input("Great job! Would you like to play again? (y/n): ") #if then statements to continue the game
        if again == "y":
            redo == True
        elif again == "n":
            break
        else:
            print("That was not an option")
            break
        
    elif num > 999: #if then statements for input validation
        print("The number needs to be 3 digits \n")
        
    elif num < 100:
        print("The number needs to be 3 digits \n")
        
    elif (x+1)!=y and (x+2)!=z:
        print("The number is not descending \n")

    elif num == "stop":
        break




