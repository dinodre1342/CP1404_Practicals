from kivy.app import App
from kivy.app import Widget

class HelloWorld(App):
    #Define a class called a Hello World inherit from App
        def build(self): #Overloading the build method from App
            #self means this build() belongs to HelloWorld.
            self.title = "Hello"
            self.root = Widget
            return self.root

HelloWorld().run() #Run the build method from HelloWorld