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
        items = [items[0], float(items[1]), int(items[2]), items[3]] #To format data structure in display
        list_items.append(items) #To passed the items into the current list from the file
    print("{} items loaded from {}".format(len(list_items), list.name)) #print the items into list format
    num += 1 #Counts every item list by 1
    list.close() #Closing the file

def list_required(): #To Display current list required of items
    incomplete_item = [] #List of curren items in the file
    total_price = [] #List of total price of the items
    for item in list_items: #To iterate each item on item list
        if item[3] == "r": #If user input = r
            incomplete_item.append(item) #Passed the object (item) to the incomplete
    if len(incomplete_item) == 0: #if the incomplete item list equals to 0
        print("No required items") #Print no required items
    else:
        new_list = sorted(incomplete_item, key=lambda priority: priority[2]) #Sort the list in place based on priority of the item
        for i, item in enumerate(new_list): #To add a counter in an iterable item list
            print("{}. {:<20s} ${:>6.2f} ({})".format(i, item[0], item[1], item[2])) #print item based on the format structure
            total_price.append(item[1]) #Passed the object of the total price of the list
        print("Total expected price for {} items: ${:.2f}".format(len(new_list), sum(total_price))) #print the total expected price of the new list


def list_completed(): #To list all of the completed items
    completed_item = [] #list of completed item
    total_price = [] #list of the total price of completed item
    for item in list_items: #To iterate each item on the list of completed items
        if item[3] == "c": #if item on file equals to "c"
            completed_item.append(item) #passed the object (item) to completed item list
    if len(completed_item) == 0: #To check whether if the completed item = 0
        print("No completed items") #print message to the user
    else:
        new_list = sorted(completed_item, key=lambda priority: priority[2]) #sort new completed item list based on desired format
        for i, item in enumerate(new_list): #To iterate each items in a row
            print("{}. {:<40s} ${:>6.2f} ({})".format(i, item[0], item[1], item[2])) #print format of the item based on 40 spaces to the left and 6 distances to the right including two decimals in place.
            total_price.append(item[1]) #Passed the object (price) to the total price
        print("Total expected price for {} items: ${:.2f}".format(len(new_list), sum(total_price))) #Print the whole total of the expected price.


def mark_as_complete(): #To select of item that want to be mark as completed
    incomplete_item = [] #list of all incomplete items
    total_price = [] #list of all the total price
    for item in list_items: #To iterate every each of the item in the list items
        if item[3] == "r": # To check whether items are still equal to required items
            incomplete_item.append(item) #passed item to the incomplete items
    if len(incomplete_item) == 0: #To check whether incomplete items equal to zero
        print("No required items") #print no more required items left
    else:
        new_list = sorted(incomplete_item, key=lambda priority: priority[2]) #sort the incomplete items based on its priority
        for i, item in enumerate(new_list): #To iterate each items row on the new list
            print("{}. {:<40s} ${:>6.2f} ({})".format(i, item[0], item[1], item[2])) #print each counter of the items list
            total_price.append(item[1]) #To passed the total price of the item based on the file
        print("Total expected price for {} items: ${:.2f}".format(len(new_list), sum(total_price)))
        print("Enter the number of an item to mark as completed")
        while True: #To check whether the item to be mark completed if its still part of the list
            try:
                marking = float(input(">>>"))
                ready_item = [] #list of all available items that wish to be completed
                marking_item = [] #list of items where on the process of marking the item
                for i in range(len(new_list)): #To iterate of the available item in the list range
                    ready_item.append(i) #passed the available items to new list
                if marking in ready_item: #To check whether marked items is part of the ready item
                    for i, item in enumerate(new_list): #To iterate every item on the new list
                        if i == marking:
                            marking_item.append(item)
                    for item in list_items:
                        if item in marking_item: #To check whether the item has been selected as marked items
                            item[3] = "c"
                            print("{} mark as completed".format(item[0])) #print message along with the selected item string
                    break
                else:
                    print("Invalid item number") #If does not met the requirement, it will print the message
            except ValueError:
                print("Invalid input; enter a number")

def add_an_item (): #To add new item to the file
    while True: #To check whether the user input of the item name
        item_name = input("Item name:")
        if len(item_name) < 1: #To check whether if the item name is empty or not
            print("Input can not be blank.") #Print message
        else:
            break
    while True:
        try:#To check of the user input equals to zero
            item_price = float(input("Price: "))
            if item_price < 0: #To check whether the item price is not equal to zero
                print ("Price must be >= $0") #print message
            else:
                break
        except ValueError: #if user inputs string instead of float
            print("Invalid input, enter a valid input.") #Print message
    while True:
        try: #To check whether the item is set onto which priority
            set_priority = input("Priority:")
            if set_priority == 0 and set_priority > 3: #To check whether the priority cant be equal and above 3
                print("Priority must 1, 2 or 3") #Print error message
            else:
                break
        except ValueError: #To check whehter user inputs float instead of string.
            print("Invalid input, enter a valid input.")
    new_item =[item_name, item_price, set_priority] #List format
    list_items.append(new_item)# passed the new added item to list_items
    print("{} $({}) (priority{:.2f}) added to shopping list".format(new_item[0], new_item[1], set_priority))

def save(): #Save file after user has edited the list required, list of completed items, and adding new file
    target_file = open("items.csv", "w") #Writing the file
    for item in list_items: #Iterate the item in list of items
        print("{},{},{},{}".format(item[0], item[1], item[2], item[3]), file=target_file)
    print("{} items saved to {}".format(len(list_items), target_file.name))
    target_file.close()

#Running the program with all of the functions in it
list_items = []
print("Shopping List 1.0 - by Andre Sardino Arno")
open_list_items()
while True: #To check where user inputs the right string to do different function of the program
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
save() #save the file to the csv file




