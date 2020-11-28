import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.widget import Widget

from widgets.playground import Playground
from widgets.doodle import Doodle

class DoodleApp(App):
    def build(self):
        return Playground()


if __name__ == '__main__':
    DoodleApp().run()