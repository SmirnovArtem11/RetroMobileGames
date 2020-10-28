import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.widget import Widget


class Playground(Widget):
    pass


class DoodleJump(App):
    def build(self):
        return Playground()


if __name__ == '__main__':
    DoodleJump().run()