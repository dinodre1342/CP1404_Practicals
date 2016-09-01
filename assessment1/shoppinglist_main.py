"""
Andre Sardino Arno

The program is to load list of saved items from a csv file. The user then can choose either list required items, add new items,
mark as completed items, or list of completed items. The program ends with saving added new items to the csv file.
Github: https://github.com/dinodre1342/CP1404_Workshops/tree/master/assessment1
"""


def menu(): #To display main menu of the shopping list and ask for user's input
    print("Menu:") #Print Menu and list of user's choices
    print("R - List required items")
    print("C - List of Completed items")
    print("A - Add new item")
    print("M - Mark an item as completed")
    print("Q - Quit")
    user_input = input(">>>") #Ask user's input based on the menu list
    user_input = user_input.upper() #Accepting if user's input is in capital letters
    return user_input #Return to menu list and user's choice


def open_list_items(): #To load list of current items from the csv file and format it preferenced display
    list = open("items.csv", 'r') #Open csv file for reading
    num = 0 #Counts start from 0
    for each in list: #To iterate number of line in file
        items = each.strip().split(",") #To split the data in each line of the file
        items = [num, items[0], items[1], items[2], items[3]] #To format data structure in display
        list_items.append(items) #To passed the items into the current list from the file
    print("{} items loaded from {}".format(len(list_items), items.name)) #print the items into list format
    num += 1 #Counts every item list by 1
    list.close() #Closing the file

def list_required(): #To Display current list required of items
    incomplete_item = [] #List of curren items in the file
    total_price = [] #List of total price of the items
    for item in list_items:
        if item[3] == "r":
            incomplete_item.append(item)
    if len(incomplete_item) == 0:
        print("No required items")
    else:
        new_list = sorted(incomplete_item, key=lambda priority: priority[2])
        for i, item in enumerate(new_list):
            print("{}. {:<20s} ${:>6.2f} ({})".format(i, item[0], item[1], item[2]))
            total_price.append(item[1])
        print("Total expected price for {} items: ${:.2f}".format(len(new_list), sum(total_price)))


def list_completed():
    completed_item = []
    total_price = []
    for item in list_items:
        if item[3] == "c":
            completed_item.append(item)
    if len(completed_item) == 0:
        print("No completed items")
    else:
        new_list = sorted(completed_item, key=lambda priority: priority[2])
        for i, item in enumerate(new_list):
            print("{}. {:<40s} ${:>6.2f} ({})".format(i, item[0], item[1], item[2]))
            total_price.append(item[1])
        print("Total expected price for {} items: ${:.2f}".format(len(new_list), sum(total_price)))


def mark_as_complete():
    incomplete_item = []
    total_price = []
    for item in list_items:
        if item[3] == "r":
            incomplete_item.append(item)
    if len(incomplete_item) == 0:
        print("No required items")
    else:
        new_list = sorted(incomplete_item, key=lambda priority: priority[2])
        for i, item in enumerate(new_list):
            print("{}. {:<40s} ${:>6.2f} ({})".format(i, item[0], item[1], item[2]))
            total_price.append(item[1])
        print("Total expected price for {} items: ${:.2f}".format(len(new_list), sum(total_price)))
        print("Enter the number of an item to mark as completed")
        while True:
            try:
                marking = float(input(">>>"))
                ready_item = []
                marking_item = []
                for i in range(len(new_list)):
                    ready_item.append(i)
                if marking in ready_item:
                    for i, item in enumerate(new_list):
                        if i == marking:
                            marking_item.append(item)
                    for item in list_items:
                        if item in marking_item:
                            item[3] = "c"
                            print("{} mark as completed".format(item[0]))
                    break
                else:
                    print("Invalid item number")
            except ValueError:
                print("Invalid input; enter a number")

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
    new_item =[item_name, item_price, set_priority]
    list_items.append(new_item)
    print("{} $({}) (priority{:.2f}) added to shopping list".format(new_item[0], new_item[1], set_priority))

def save():
    target_file = open("items.csv", "w")
    for item in list_items:
        print("{},{},{},{}".format(item[0], item[1], item[2], item[3]), file=target_file)
    print("{} items saved to {}".format(len(list_items), target_file.name))
    target_file.close()


list_items = []
open_list_items()
print("Shopping List 1.0 - by Andre Sardino Arno")
print("{} items loaded from items.csv".format(len(list_items)))

while True:
    user_input = menu()
    if user_input == "R":
        list_required()
    elif user_input == "C":
        list_completed()
    elif user_input == "M":
        mark_as_complete()
    elif user_input == "A":
        add_an_item()
    elif user_input == "Q":
        break
save()




