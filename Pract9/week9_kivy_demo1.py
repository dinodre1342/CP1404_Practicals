from kivy.app import App
from kivy.lang import Builder

class ButtonApp(App):

    def build(self):
        self.title = "My Button App"
        self.root = Builder.load_file("button_app_kivy.kv")

    def press_b1(self):
        string_input = self.root.ids.input1.text
        print("I got the data: ", string_input)

ButtonApp().run()