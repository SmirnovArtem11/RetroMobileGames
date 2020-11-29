import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config

from widgets.playground import Playground
from widgets.doodle import Doodle

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '414')
Config.set('graphics', 'height', '736')

class DoodleApp(App):
    def build(self):
        playground = Playground()
        playground.start()
        return playground


if __name__ == '__main__':
    DoodleApp().run()