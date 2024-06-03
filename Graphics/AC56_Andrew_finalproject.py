#Phrases that are too long won't fit inside the window and I was unable to find a fix to that.
#I used sources from W3Schools, StackOverflow, and Reddit.

from graphics import *

def string_to_binary(text):
    binary_list = [] #initialize an empty list
    for char in text:
        binary = bin(ord(char))[2:].zfill(8) #convert character to its ASCII value and then to a binary string without the '0b' prefix
        binary_list.extend(map(int, binary)) #convert binary string to a list of integers (0s and 1s)

    return binary_list

def xor_encrypt(text, key):
    encrypted_text = []
    for i in range(len(text)):
        encrypted_text.append(text[i] ^ key[i % len(key)]) #XOR each bit of the text with the corresponding bit of the key and repeat the key if needed
    return encrypted_text

def draw_truth_table(win, x, y, a, b, result):
    input_a_text = Text(Point(x, y), f'{a}') #draw the text for the first input bit
    input_a_text.setSize(8) #set text size to 8
    input_a_text.draw(win)
    
    xor_text = Text(Point(x + 10, y), '^') #draw ^ to show the XOR process
    xor_text.setSize(8)
    xor_text.draw(win)

    input_b_text = Text(Point(x + 20, y), f'{b}') #draw the text for the second input bit
    input_b_text.setSize(8)
    input_b_text.draw(win)
    
    equals_text = Text(Point(x + 30, y), '=') #draw the = sign
    equals_text.setSize(8)
    equals_text.draw(win)
    
    result_text = Text(Point(x + 40, y), f'{result}') #draw the text for the result of the XOR operation
    result_text.setSize(8)
    result_text.draw(win)

def display_tables(win, binary_text, binary_key, encrypted_binary, start_index, end_index, start_x, start_y, table_height):
    for item in win.items[:]: #clear the window by undrawing all current items
        item.undraw()

    #craw the plaintext in binary at the top of the window
    plaintext_text = Text(Point(400, 50), "Plaintext (ASCII): " + " ".join(map(str, binary_text)))
    plaintext_text.setSize(10) #set text size to 10
    plaintext_text.draw(win)

    #draw the key in binary below the plaintext
    key_text = Text(Point(400, 70), "XOR Key (ASCII): " + " ".join(map(str, binary_key)))
    key_text.setSize(10)
    key_text.draw(win)

    for i in range(start_index, end_index): #draw the XOR truth tables from start_index to end_index
        y = start_y + (i - start_index) * table_height #calculate the y position for each table row
        # Get the corresponding bits from the plaintext and key
        a = binary_text[i]
        b = binary_key[i % len(binary_key)]
        result = a ^ b #calculate the result of the XOR operation, ie: 1^0=1, 1^1=0, 0^1=1, 1^1=0
        draw_truth_table(win, start_x, y, a, b, result) #draw the truth table for the current bits

    instructions_text = Text(Point(400, 780), "Use 'Up' and 'Down' arrows to scroll. Press 'Escape' to exit.")
    instructions_text.setSize(10)
    instructions_text.draw(win)

    encrypted_binary_text = Text(Point(400, 740), "Encrypted Binary: " + " ".join(map(str, encrypted_binary)))
    encrypted_binary_text.setSize(10)
    encrypted_binary_text.draw(win)

def main():
    text = input("Enter the text to encrypt: ")
    key = input("Enter the XOR key: ")

    binary_text = string_to_binary(text) #convert the text and key to binary
    binary_key = string_to_binary(key)

    encrypted_binary = xor_encrypt(binary_text, binary_key) #encrypt binary text with the binary key

    win = GraphWin("XOR Encryption Process", 800, 800) #initialize the window
    win.setBackground("white")

    table_height = 30 #height of each truth table row
    start_x = 380 #starting x position for the truth tables
    start_y = 100 #starting y position for the truth tables
    visible_tables = 18 #number of tables that can be displayed in the window vertically

    total_tables = len(binary_text) #number of truth tables to display
    tables_per_page = visible_tables #set the number of tables to display per page

    #initial display of truth tables and displaying the first set of tables
    display_tables(win, binary_text, binary_key, encrypted_binary, 0, min(tables_per_page, total_tables), start_x, start_y, table_height)

    current_start_index = 0

    #a loop to "scroll"
    while True:
        key = win.getKey()
        if key == "Down": #scroll down if not at the end
            if current_start_index + tables_per_page < total_tables:
                current_start_index += visible_tables
        elif key == "Up": #scroll up if not at the beginning
            if current_start_index - visible_tables >= 0:
                current_start_index -= visible_tables
        elif key == "Escape": #breal if the person hits escape
            break

        #update the displayed portion of the truth tables
        display_tables(win, binary_text, binary_key, encrypted_binary, current_start_index, min(current_start_index + tables_per_page, total_tables), start_x, start_y, table_height)

    win.close()

if __name__ == "__main__":
    main()
