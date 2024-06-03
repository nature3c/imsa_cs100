import random

#4.1
def binary():
    print("""\nWelcome to the number converter. Please enter a
whole number, in base 10, to be converted to binary.""")

    decimal_num = int(input("Please enter the number to be converted to binary: "))

    binary = "" #declare an empty string to be used later
    boolean = ""

    a = decimal_num #set different variables to the decimal number because not doing that will affect the original number and i do not want that
    b = decimal_num
    count = 0 #TRY

    while a > 0: #convert to binary
        part = a%2 #find the remainder
        a = a//2 #find the quotient but as an int ignoring the remainder

        binary = binary + str(part)#add that number to the binary string

    while b > 0: #create the binary chain exlcuding the original number
        part2 = b//2 #get the quotient ignoring the remainder
        b = b//2 #sets the b value to the new quotient for the next iteration
        
        boolean = boolean + "-" + str(part2) #add to the string
        count += 1 #TRY

    reverse = binary[::-1] #reverse the string
    reverse_boolean = boolean[::-1]

    print("\nThe binary nuber is: " + reverse)
    print("The chain is: " + reverse_boolean + str(decimal_num))
    print("There are " + str(count+1) + " numbers in the chain")

#4.1 but octal
def octal():
    print("""\nWelcome to the number converter. Please enter a
whole number, in base 10, to be converted to octal.""")

    decimal_num = int(input("Please enter the number to be converted to binary: "))

    binary = "" #declare an empty string to be used later
    boolean = ""

    a = decimal_num #set different variables to the decimal number because not doing that will affect the original number and i do not want that
    b = decimal_num
    count = 0 #TRY

    while a > 0: #convert to binary
        part = a%8 #find the remainder
        a = a//8 #find the quotient but as an int ignoring the remainder

        binary = binary + str(part)#add that number to the binary string

    while b > 0: #create the binary chain exlcuding the original number
        part2 = b//8 #get the quotient ignoring the remainder
        b = b//8 #sets the b value to the new quotient for the next iteration
        
        boolean = boolean + "-" + str(part2) #add to the string
        count += 1 #TRY

    reverse = binary[::-1] #reverse the string
    reverse_boolean = boolean[::-1]

    print("\nThe binary nuber is: " + reverse)
    print("The chain is: " + reverse_boolean + str(decimal_num))
    print("There are " + str(count+1) + " numbers in the chain")
    
#4.2
def vowel_count():
    print("""\nWelcome, this program will find the vowels in
your sentence.""")

    sentence = input("Please input the sentence: ").lower()
    vowels = ["a", "e", "i", "o", "u"]

    count = 0

    for char in sentence:
        if char in vowels:
            count += 1
        
    print("Number of vowels:", count)
#end of 4.2

#4.3
def reverse():
    print("\nWelcome to the phrase/sentence reverser")
    string = input("Please input the string or phase: ")

    reverse_string = string[::-1] #slicing to reverse the string: means start at end of the string, end at position 0 (start), and step -1 (backwards)
    print("The reverse is: " + reverse_string)

#4.4
def random_list():
    print("\nWelcome to random list")

    random_list = [random.randint(1,100) for i in range(100)]
    print("The random numbers are: " + str(random_list))

    list_sum = sum(random_list)
    print("The sum of the numbers in the list is: " + str(list_sum))

    average = list_sum / 100
    print("The average of the list is: " + str(average))

#4.5
def replacer():
    input_str = input("""\nEnter the string, old substring, and new substring separated by spaces
: """)

    original, old, new = [str(n) for n in input_str.split(' ')] #split into 3 strings

    new_string = "" #initiate an empty string

    for char in original: #go through every character in OG string
        if char == old: #if the character matches the old char then replace with new characters
            new_string += new
        else:
            new_string += char #otherwise leave it the same

    print(new_string)
    
#program to run the functions

on = True #set on to True so loop runs forever

while on == True:
    print("""
1. Decimal number to binary converter
2. Decimal number to octal converter
3. Find the number of vowels in a sentence
4. Reverse a sentence
5. Create a list with random numbers
6. Replace string characters
7. Quit""")
    
    program = str(input("Please choose what program you would like to run: "))
    
    if program == str(1): #changes the number to string so I don't have to do more work
        binary()
        
        option = input("\nWould you like to try out my functions again? (y/n): ")
        if option == "y":
            continue
        elif option == "n":
            break
        else:
            break

    elif program == str(2):
        octal()
        
        option = input("\nWould you like to try out my functions again? (y/n): ")
        if option == "y":
            continue
        elif option == "n":
            break
        else:
            break
    
    elif program == str(3): 
        vowel_count()
        
        option = input("\nWould you like to try out my functions again? (y/n): ")
        if option == "y":
            continue
        elif option == "n":
            break
        else:
            break
        
    elif program == str(4):
        reverse()

        option = input("\nWould you like to try out my functions again? (y/n): ")
        if option == "y":
            continue
        elif option == "n":
            break
        else:
            break
        
    elif program == str(5):
        random_list()

        option = input("\nWould you like to try out my functions again? (y/n): ")
        if option == "y":
            continue
        elif option == "n":
            break
        else:
            break
        
    elif program == str(6):
        replacer()

        option = input("\nWould you like to try out my functions again? (y/n): ")
        if option == "y":
            continue
        elif option == "n":
            break
        else:
            break
        
    elif program == str(7):
        break
    
    else:
        print("\nThat was not an option please try again")
        continue
