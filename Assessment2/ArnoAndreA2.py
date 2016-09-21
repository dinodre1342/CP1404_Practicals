from kivy.app import App
from kivy.lang import Builder

class Shopping_list(App):
    def builder(self):
        self.title = "Shopping List"
        self.root = Builder.load_file('shopping_list.kv')
        return self.root

Shopping_list().run()