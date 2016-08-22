from kivy.app import App
from kivy.lang import Builder

class Demo2(App):
    def build(self):
        self.title = "Demo2"
        self.root = Builder.load_file('demo2.kv')
        return self.root

    def button_press(self):
        print ("Button has been clicked.")

Demo2().run()