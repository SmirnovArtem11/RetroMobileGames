import kivy
kivy.require('1.10.1')

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Playground(Widget):
    doodle = ObjectProperty(None)
    platforms = ObjectProperty(None)
    
    def start(self):
        self.doodle.start()
        self.platforms.start()
    
    def on_touch_down(self, touch):
        x_pos = touch.spos[0]
        if x_pos <= 0.5:
            self.doodle.move_left()
        else:
            self.doodle.move_right()
    
    def on_touch_up(self, touch):
        self.doodle.move_stop()
