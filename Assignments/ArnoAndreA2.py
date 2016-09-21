from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class Shopping_list(App):

    def __init__(self):
        list_item = []
        list_required = []
        list_completed = []
        list_add_item = []
        mark_as_completed = []
        incomplete_item = []
        total_price = []
        self.list_item = list_item
        self.list_required = list_required
        self.list_completed = list_completed
        self.list_add_item = list_add_item
        self.total_price = total_price
        self.mark_as_completed = mark_as_completed
        self.incomplete_item = incomplete_item
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
        else:
            continue

        self.root.ids.list_item.add_widget (temp_button)

    def press_list_completed (self):
        for items in self.list_completed:
            if len(self.list_required) == 0:
                self.status_text = "No Completed Items."
            else len(self.)




    def press_item_to_mark_completed (self):
        for items in self.list_required:



    def press_additem (self, instance):
        name = instance.text
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
        self.root.ids.new_item_price.text = ""
        self.root.ids.new_item_priority.text = ""





Shopping_list().run()