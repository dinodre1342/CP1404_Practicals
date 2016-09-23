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
        self.list_item = list_item
        mode = "required"
        self.mode = mode
        item_file_open = open("items.csv", "r") #Opening the file for reading
        for items in item_file_open: #Iterate through items in file
            name, price, priority, status = items.strip().split(",")
            item = "{},{:.2f},{},{}".format(name, float(price), priority, status)
            list_item.append(item)



    def builder(self): #Building the GUI
        self.title = "Shopping List" #Title Name
        self.root = Builder.load_file('shopping_list.kv')
        self.start_run() #Start method
        return self.root

    def create_item_list(self, action_mode): #To make the item list button
        self.root.ids.list_item.clear.widgets() #Clearing list of mark completed except the default list required items
        if self.mode == "required":
            for items in self.list_item: #Iterate items in list item
                if items[3] == "r":
                    temp_button = Button(text=items[0])
                    temp_button.bind(on_release=self.mark_complete)
                    if items[2] == "1": #Set condition of the background color based on the item priority 1, 2, 3
                        temp_button.background_color = 1, 0, 0, 1
                    elif items[2] == "2":
                        temp_button.background_color = 0, 1, 0, 1
                    elif items[2] == "3":
                        temp_button.background_color = 0, 0, 1, 1
        elif self.mode == "completed":
            for items in self.list_item: #Iterate items in list item
                if items[3] == "c":
                    temp_button = Button(text=items[0])
                    temp_button.bind(on_release=self.show_description)
                    if items[2] == "1": #Set condition of the background color based on the item priority 1, 2, 3
                        temp_button.background_color = 1, 0, 0, 1
                    elif items[2] == "2":
                        temp_button.background_color = 0, 1, 0, 1
                    elif items[2] == "3":
                        temp_button.background_color = 0, 0, 1, 1
        self.root.ids.list_item.add_widget(temp_button)


    def list_required(self):
        self.mode = "required"
        required_item = []
        required_item_price = []
        for items in self.list_item:
            if items[3]=="r":
                required_item.append(items)
                required_item_price.append(items[1])
        if len(required_item)== 0:
            self.status_text = "No required items"
        elif len(required_item) >0:
            self.status_text = "Press on the item to mark as complete"
        self.create_item_list()
        self.root.ids.total_price = sum(required_item_price)

    def list_completed(self): #Command button when pressed in 'list completed'
        self.mode = "completed"
        completed_item = []
        for items in self.list_item:
            if items[3] == "r":
                completed_item.append(items)
        if len(self.list_item) == 0:
            self.status_text = "No Completed Items."
        elif len(self.list_item) > 0:
            self.status_text = " Press on the item to show details."
        self.create_item_list()


    def mark_complete(self,instance): #Function as to mark selected items as mark completed items
        for items in self.list_item:
            if items == instance.text:
                items[3] = "c"


    def show_description(self,instance): #Function to show description if whether the item has been added completely
        for items in self.list_item:
            if items == instance.text:
                self.status_text = "{} ${}, priority {} is completed".format(items[0], items[1], items[2])

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

    def on_stop(self): #Program ends by saving all of the items to csv
        output_file = open("items.csv", "w")
        for items in self.list_item:
            print(items, file=output_file)
        print ("{} items have been saved to items.csv".format(len(self.list_item)))
        output_file.close()

Shopping_list().run()