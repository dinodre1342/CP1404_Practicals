"""
Andre Sardino Arno
22 September 2016
This program allows to load items from the csv file and implemented to the GUI interfaces of the Kivy. It allows list required, list completed, add new items, based on their priority level. The program ended by saving all of the current items to the csv file.
https://github.com/dinodre1342/CP1404_Workshops/tree/master/Assignments"
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class Shopping_list(App): #Whole Class of the Shopping List
    status_text = StringProperty()

    def __init__(self): #Initialize for the class
        super(Shopping_list, self).__init__() #Inherit from the super class
        list_item = [] #List 'list item' that can be later used in different function
        list_completed = [] #list 'list completed' items ~
        list_add_item = [] #list 'list_add_item' items ~
        mark_as_completed = [] # list that can be used later as mark_as_completed
        total_price = [] #list that can be later used as total_price
        item_priority = [] #list that can later use as item priority
        self.item_priority = item_priority #Variable assignment to class
        self.list_item = list_item
        self.list_completed = list_completed
        self.list_add_item = list_add_item
        self.total_price = total_price
        self.mark_as_completed = mark_as_completed
        item_file_open = open("items.csv", "r") #Opening the file for reading
        for items in item_file_open: #Iterate through items in file
            list_item.append(items)


    def builder(self): #Building the GUI
        self.title = "Shopping List" #Title Name
        self.root = Builder.load_file('shopping_list.kv')
        self.start_run() #Start method
        return self.root

    def create_item_list(self, action_mode): #To make the item list button
        self.total_price.clear()
        self.list_add_item.clear()
        self.list_completed()
        self.root.ids.list_item.clear.widgets() #Clearing list of mark completed except the default list required items

        for items in self.list_item: #Iterate items in list item
            temp_button = Button(text=items.name)
        if action_mode == "List Required":
            temp_button.bind(on_release=self.press_to_show_listitem)
        elif action_mode == "List Completed":
            temp_button.bind(on_release=self.press_to_show_completeditems)
        elif action_mode == "Add Item":
            temp_button.bind(on_release=self.press_to_add_item)

        if items.priority() == "1": #Set condition of the background color based on the item priority 1, 2, 3
            temp_button.background_color = 1, 0, 0, 1
        elif items.priority() == "2":
            temp_button.background_color = 0, 1, 0, 1
        elif items.priority() == "3":
            temp_button.background_color = 0, 0, 1, 1


        self.root.ids.list_item.add_widget (temp_button)

    def press_to_show_completeditems (self): #Command button if pressed on "List Completed"
        for items in self.list_completed: #iterate items based on whether items have been check or not as completed items
            if len(self.list_item) == 0:
                self.status_text = "No Completed Items."
            elif len(self.list_item) > 0:
                self.status_text = " You have mark to completed items."


    def press_to_add_item (self, instance): #Command button if pressed on add items
        name = instance.text
        price = instance.text
        priority = instance.text
        for items in self.list_add_item: #Iterate items if user fill in the blank empty
            if items.name() == name:
                if len(self.list_add_item):
                    if items.name() == "":
                        self.status_text = "Please fill in the name of the item"
                    elif items.price(name) == "":
                        self.status_text = "Please fill in the price of the item"
                    elif items.priority(name) == "":
                        self.status_text = "Please fill in the priority of the item"
                else:
                    self.add_item_text_check.append = "Name: {}, Price: ${}, Priority:{}".format(items.name, items.price, items.priority)

    def clear_input (self): #Clearing the popup box field
        self.root.ids.new_item_name.text = ""
        self.root.ids.enter_item_price.text = ""
        self.root.ids.enter_priority.text = ""

    def start_run(self): #How the start of the program runs
        self.create_item_list(action_mode='list')
        self.root.ids.total_price.background_color = 0, 0, 0, 0
        self.root.ids.list_item.background_color = 1, 0, 0, 1
        self.root.ids.list_completed.background_color = 0, 1, 0, 1
        self.root.ids.mark_completed = 0, 0, 1, 1

    def list_item(self): #listing all of the required items as start of the program
        self.create_item_list(action_mode='list')
        self.root.ids.total_price.background_color = 0, 0, 0, 0
        self.root.ids.list_item.background_color = 1, 0, 0, 1
        self.root.ids.list_completed.background_color = 0, 1, 0, 1
        self.root.ids.mark_completed = 0, 0, 1, 1


    def list_completed (self): #listing all of the mark completed or has not mark in 'list mode'
        self.create_item_list(action_mode= 'list')
        self.root.ids.total_price.background_color = 0, 0, 0, 0
        self.root.ids.list_item.background_color = 1, 0, 0, 1
        self.root.ids.list_completed.background_color = 0, 1, 0, 1
        self.root.ids.mark_completed = 0, 0, 1, 1
        self.status_text =  "Select available items to mark as completed"

    def total_price (self): #label to show total price of the items (either list required or just added items)
        for items in self.total_price:
            sum(total_pr)
            print("The total price ")



    def confirm_action(self): #Confirm adding new item
        for name in self.list_add_item:
            for items in self.list_item:
                if name == items.name:
                    items.add()
        for name in self.list_completed:
            for items in self.list_item:
                if name == items.name:
                    items.completed()
        self.start_run()

    def finish_stop (self): #Program ends by saving all of the items to csv
        output_file = open("items.csv", "w")
        for items in self.list_item:
            print(items, file=output_file)
        print ("{} items have been saved to items.csv".format(len(self.list_item)))
        output_file.close()

Shopping_list().run()