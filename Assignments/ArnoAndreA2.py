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
        total_price = []
        self.list_item = list_item
        self.list_required = list_required
        self.list_completed = list_completed
        self.list_add_item = []
        self.total_price = []
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
            temp_button =


    def clear_input (self):
        self.root.ids.new_item_name.text = ""
        self.root.ids.new_item_price.text = ""
        self.root.ids.new_item_priority.text = ""





Shopping_list().run()