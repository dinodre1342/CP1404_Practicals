from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class Shopping_list(App):

    def __init__(self):
        list_item = []
        list_completed = []
        list_add_item = []
        mark_as_completed = []
        total_price = []
        item_priority = []
        self.item_priority = item_priority
        self.list_item = list_item
        self.list_completed = list_completed
        self.list_add_item = list_add_item
        self.total_price = total_price
        self.mark_as_completed = mark_as_completed
        item_file_open = open("items.csv", "r")
        for items in item_file_open:
            list_item.append(items)

    def builder(self):
        self.title = "Shopping List"
        self.root = Builder.load_file('shopping_list.kv')
        self.start_run()
        return self.root

    def create_item_list(self, action_mode):
        self.total_price.clear()
        self.list_add_item.clear()
        self.list_completed()
        self.root.ids.list_item.clear.widgets()

        for items in self.list_item:
            temp_button = Button(text=items.name)
        if action_mode == "List Required":
            temp_button.bind(on_release=self.press_to_show_listitem)
        elif action_mode == "List Completed":
            temp_button.bind(on_release=self.press_to_show_completeditems)
        elif action_mode == "Add Item":
            temp_button.bind(on_release=self.press_to_add_item)

        if items.priority() == "1":
            temp_button.background_color = 1, 0, 0, 1
        elif items.priority() == "2":
            temp_button.background_color = 0, 1, 0, 1
        elif items.priority() == "3":
            temp_button.background_color = 0, 0, 1, 1


        self.root.ids.list_item.add_widget (temp_button)

    def press_to_show_completeditems (self):
        for items in self.list_completed:
            if len(self.list_item) == 0:
                self.status_text = "No Completed Items."
            else len(self.list_item) >= 0:
                self.status_text = " You have selected completed items."


    def press_to_add_item (self, instance):
        name = instance.text
        price = instance.text
        priority = instance.text
        for items in self.list_add_item:
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


    def clear_input (self):
        self.root.ids.new_item_name.text = ""
        self.root.ids.enter_item_price.text = ""
        self.root.ids.enter_priority.text = ""

    def start_run(self):
        self.create_item_list(action_mode='list')
        self.root.ids.total_price.background_color = 0, 0, 0, 0
        self.root.ids.list_item.background_color = 1, 0, 0, 1
        self.root.ids.list_completed.background_color = 0, 1, 0, 1
        self.root.ids.mark_completed = 0, 0, 1, 1

    def list_required (self):
        self.create_item_list(action_mode='list')
        self.root.ids.total_price.background_color = 0, 0, 0, 0
        self.root.ids.list_item.background_color = 1, 0, 0, 1
        self.root.ids.list_completed.background_color = 0, 1, 0, 1
        self.root.ids.mark_completed = 0, 0, 1, 1

    def list_completed (self):
        self.create_item_list(action_mode= 'list')
        self.root.ids.total_price.background_color = 0, 0, 0, 0
        self.root.ids.list_item.background_color = 1, 0, 0, 1
        self.root.ids.list_completed.background_color = 0, 1, 0, 1
        self.root.ids.mark_completed = 0, 0, 1, 1
        self.status_text =  "Select available items to mark as completed"

    def confirm_action(self):
        for name in self.list_add_item:
            for items in self.list_item:
                if name == items.name:
                    items.add()
        for name in self.list_completed:
            for items in self.list_item:
                if name == items.name:
                    items.completed()
        self.start_run()

    def finish_stop (self):
        output_file = open("items.csv", "w")
        for items in self.list_item:
            print(items, file=output_file)
        print ("{} items have been saved to items.csv".format(len(self.list_item)))
        output_file.close()

Shopping_list().run()