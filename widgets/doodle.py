import kivy
kivy.require('1.10.1')

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

class Doodle(Widget):
    doodle_img = ObjectProperty(None)
    jump_sound_src = StringProperty()
    jump_right_img_src = StringProperty()
    jump_left_img_src = StringProperty()
    
    def move_right(self):
        self.doodle_img.source = self.jump_right_img_src
        
        duration = 0.8 * (Window.size[0] - self.pos[0]) / Window.size[0]
        anim = Animation(x = Window.size[0], t='in_quad', d=duration)
        anim.start(self)
        anim.start(self.doodle_img)
    
    def move_left(self):
        self.doodle_img.source = self.jump_left_img_src
        
        duration = 0.8 * self.pos[0] / Window.size[0]
        anim = Animation(x = -self.width, t='linear', d=duration)
        anim.start(self)
        anim.start(self.doodle_img)
    
    def move_stop(self):
        Animation.stop_all(self, 'x')
        Animation.stop_all(self.doodle_img, 'x')
    
    def jump(self):
        if self.jump_sound_src:
            jump_sound = SoundLoader.load(self.jump_sound_src)
            jump_sound.play()
            
        self.pos[1] = self.pos[1] + 0.1 
        
        anim = Animation(y = self.y + self.height * 3, t='out_quad', d=0.4)
        anim.bind(on_complete=self.fall)
        anim.start(self)
        anim.start(self.doodle_img)
    
    def fall(self, *args):
        duration = 0.4/3 * self.pos[1] / self.height
        anim = Animation(y = 0, t='in_quad', d=duration)
        anim.start(self)
        anim.start(self.doodle_img)
    
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
        
        if self.pos[1] <= 0: 
            self.jump()
    