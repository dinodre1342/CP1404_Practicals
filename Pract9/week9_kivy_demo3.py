from kivy.app import App
from kivy.lang import Builder

class PopOutApp(App):
    def build(self):
        self.title = "Pop Out Demo"
        self.root = Builder.load_file("pop.kv")

    def showit(self):
        self.root.ids.popup1.open()

    def removeMe(self):
        self.root.ids.popup1.dismiss()

PopOutApp().run()