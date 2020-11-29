import kivy
kivy.require('1.10.1')

from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class Playground(Widget):
    doodle = ObjectProperty(None)
    
    def start(self):
        Clock.schedule_interval(self.doodle.update, 0.001)
        print("aaaaaaaaaa, I'm alive!!!")
    
    def on_touch_down(self, touch):
        x_pos = touch.spos[0]
        if x_pos <= 0.5:
            self.doodle.move_left()
        else:
            self.doodle.move_right()
    
    def on_touch_up(self, touch):
        self.doodle.move_stop()
