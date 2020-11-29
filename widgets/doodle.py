import kivy
kivy.require('1.10.1')

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.core.window import Window 

class Doodle(Widget):
    doodle_img = ObjectProperty(None)
    
    def move_right(self):
        duration = 0.4 * (Window.size[0] - self.pos[0]) / Window.size[0]
        anim = Animation(x = Window.size[0], t='linear', d=duration)
        anim.start(self)
        anim.start(self.doodle_img)
    
    def move_left(self):
        duration = 0.4 * self.pos[0] / Window.size[0]
        anim = Animation(x = -self.width, t='linear', d=duration)
        anim.start(self)
        anim.start(self.doodle_img)
    
    def move_stop(self):
        Animation.stop_all(self, 'x')
        Animation.stop_all(self.doodle_img, 'x')
    
    def update(self, *args):
        if self.pos[0] >= Window.size[0] - self.width/2:
            self.pos[0] = -self.width/2 + 1
            self.doodle_img.pos[0] = -self.width/2 + 1
            
            self.move_stop()
            self.move_right()
        elif self.pos[0] <= -self.width/2:
            self.pos[0] = Window.size[0] - self.width/2 - 1
            self.doodle_img.pos[0] = Window.size[0] - self.width/2 - 1
            
            self.move_stop()
            self.move_left()
    