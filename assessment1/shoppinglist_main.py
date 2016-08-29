"""
Andre Sardino Arno

The program is to load list of saved items from a csv file. The user then can choose either list required items, add new item,
mark completed items, or list of completed items. The program ends with saving added new items to the csv file.
"""


def menu():
    print("Menu:")
    print("R - List required items")
    print("C - List of Completed items")
    print("A - Add new item")
    print("M - Mark an item as completed")
    print("Q - Quit")
    user_input = input(">>>")
    user_input = user_input.upper()
    return user_input


def open_list_items():
    list = open("items.csv", 'r')
    num = 0
    for each in list:
        items = each.strip().split(",")
        items = [num, items[0], items[1], items[2], items[3]]
        list_items.append(items)
        num += 1
    list.close()

def listing_current_items():
    price = 0
    for items in list_items:
        print("{}. {:<20s} $ {:>6.2f}".format(items[0], items[1], float(items[2])))
        price += float(items[2])
    print("Total expected price for {} items: $ {:>6.2f}".format(len(list_items), price))

def mark_complete():
    price = 0
    for items in list_items:
        print("{}. {:<20s} $ {:>6.2f}".format(items[0], items[1], float(items[2])))
        price += float(items[2])
    while True:
        enter_items = input("Enter the number of item to mark as completed:")
        if enter_items != "{}*".format(int(items)):
            print("Invalid Input!")
        else:
            print("{} marked as completed.".format(items[0]))
            break

def add_an_item ():
    while True:
        item_name = input("Item name:")
        if len(item_name) < 1:
            print("Input can not be blank.")
        else:
            break
    while True:
        try:
            item_price = float(input("Price: "))
            if item_price != float:
                print ("Price must be >= $0")
            else:
                break
        except ValueError:
            print("Invalid input, enter a valid input.")
    while True:
        try:
            set_priority = input("Priority:")
            if set_priority == 0 and set_priority > 3:
                print("Priority must 1, 2 or 3")
            else:
                break
        except ValueError:
            print("Invalid input, enter a valid input.")
    new_item = [len(list_items + items_added), item_name, item_price, set_priority]








items_added = []
list_items = []
open_list_items()
print("Shopping List 1.0 - by Andre Sardino Arno")
print("{} items loaded from items.csv".format(len(list_items)))

while True:
    user_input = menu()
    if user_input == "R":
        listing_current_items()
    elif user_input == "M":
        mark_complete()
    elif user_input == "C":
        if user_input :
            print("No Completed items.")
        elif mark_complete():





