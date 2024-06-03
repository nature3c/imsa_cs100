import time 

f = float(input('Enter the farenheit temperature: ')) # the temp in farenheit
c = float((f-32)*(5/9)) # the math conversion as a float because its not going to be a whole number
print('The temperature in Celcius is: ' + str(c)) # print with the celcius value casted to string

print('\n')

time.sleep(3)

x = float(input('Enter the side of a square: ')) # input the float in case it has decimals
a = x*x # the math which is just x^2
print('The area of the square is: ' + str(a)) #print statement and a casted to a string

print('\n')

time.sleep(3)

print('\  |  / \n  @ @ \n \\"""/') #\\ is used to print \

print('\n')

print('  _______ \n // 6 6 \\\\ \n \\\\\\_v_// \n   \\~/\\~/~ \n    / @ \\')

print('\n')

time.sleep(3)

color = str(input('Enter your favorite color: ')) # color as a string
top = (color + ' ') * 10 # print red and a space 10 times
char = sum(1 for c in color if c.isalpha()) # find number of characters in string
#print(char) used this to debug
space1 = str(' ') # called a space using space1 so that it looks good
space = (space1*char)*8 + (space1*9)
#there are 8 words in between the first and last word so there must be that many spaces times
#the amount of characters in the word. Along with the spaces between the first and last words which is 9 
print(top + '\n' + color + space + color + '\n' + color + space + color + '\n' + top)
# above is the final print statement with \n to make new lines

print('\n')

time.sleep(3)

answer = input('Do you like Python? (type yes or no): ') #question and input
if answer == 'yes': # output if answer is yes
    print('That is great!')
elif answer == 'no': # output if answer is no
    print('That is dissapointing')
else: # output if answer is not yes or no
    print('That is not an answer to my question')

print('\n')

time.sleep(3)

age = int(input("What is your age?: ")) # integer input
if age < 18: # case for under 18
    print("You are not old enough to vote.")
elif 18 < age < 25: # case for over 18 but less than 25
    print("You are old enough to vote, but not to rent a car.")
else: # case for any age over 25
    print("You are old enough to vote and rent a car.")

print('\n')


