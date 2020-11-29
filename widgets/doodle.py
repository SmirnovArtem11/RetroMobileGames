import kivy
kivy.require('1.10.1')

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.core.window import Window 

class Doodle(Widget):
    doodle_img = ObjectProperty(None)
    
    def move_right(self):
        anim = Animation(x = Window.size[0] + self.width/2, t='linear', duration=.5)
        anim.start(self)
        anim.start(self.doodle_img)
    
    def move_left(self):
        anim = Animation(x = -self.width/2, t='linear', duration=.5)
        anim.start(self)
        anim.start(self.doodle_img)
    
    def move_stop(self):
        Animation.stop_all(self, 'x')
        Animation.stop_all(self.doodle_img, 'x')