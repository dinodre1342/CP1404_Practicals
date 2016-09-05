
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

class TicTacToe(App):

    Config.set("graphics", "width", "200")
    Config.set("graphics", "height", "200")

    def builder(self):
        self.title = "Tic Tac Toe"
        self.root = Builder.load_file("tictactoe.kv")

    def pressed(self, kv_obj):
        print(kv_obj.text)
        if kv_obj.text == "_":
            kv_obj.text = "X"
        elif kv_obj.text == "X":
            kv_obj.text = "O"
        else:
            kv_obj.text = "_"


TicTacToe().run()