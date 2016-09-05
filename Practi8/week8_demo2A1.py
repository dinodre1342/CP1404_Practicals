"""
•	display a welcome message with your name in it
•	display a menu for the user to choose from
•	return to the menu and loop until the user chooses to quit
•	error-check user inputs as demonstrated in the sample output
•	start by loading a CSV (Comma Separated Values) file of items that are in stock for hire;
a sample CSV file is provided for you
•	(when the user chooses list) display a neatly formatted list of all the required items with their prices lined up and priorities
•	(when the user chooses show completed) display a similarly formatted list of completed items
•	(when the user chooses add) prompt for the item’s name, price and priority, error-checking each of these, then add the item to the list in memory
•	(when the user chooses complete) display the same list of required items, then allow the user to choose one (error-checked), then change that item to completed
o	if no items are required, then a message should be displayed and the user returned to the menu
•	(when the user chooses quit) save the items to the CSV file, overwriting the file contents
"""

def print_menu():
    menu_str = """
    Shopping List 1.0 - by Yok Yen
    Menu:
    R - List required items
    C - List completed items
    A - Add new item
    M - Mark an item as completed
    Q - Quit
"""
    print(menu_str)

def get_input(valid_input):
    user_input = input(">>>").lower()
    if user_input not in valid_input:
        user_input = input(">>>").lower()
    return user_input

def load_csv(filename):
    file_pointer = open(filename, "r")
    for each in file_pointer:
        print(each)
    file_pointer


while True:
    print_menu()
    user_choice = get_input(["r", "c", "a", "m", "q"])
    if user_choice == "q":
        break
    elif user_choice == "r":
        load_csv("data.csv")

print("Program ended")