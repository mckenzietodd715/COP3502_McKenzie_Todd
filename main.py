# McKenzie Todd Lab 6

def encode(data_string):
    res = ""
    for num in data_string:
        # converts each number in the string to an integer
        old_value = int(num)
        if old_value <= 6:
            new_value = old_value + 3
        if old_value == 7:
            new_value = 0
        if old_value == 8:
            new_value = 1
        if old_value == 9:
            new_value = 3
        # returns the value to a string
        value = str(new_value)
        # combines the numbers into a string
        res += value
    return res

def decode(data_string):
    pass

if __name__ == '__main__':
    # loop to continue function until user quits
    while True:
        # display the menu
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        print()

        # user input for menu option
        user_opt = input("Please enter an option: ")