import kivy
kivy.require('1.10.1')

from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock

class PlatformFabrica(Widget):
    doodle = ObjectProperty(None)
    
    platform_green_src = StringProperty(None)
    platform_green_size = ListProperty(None)
    
    platforms_green_pos = []
    
    def start(self):
        for i in range(1,10):
            with self.canvas:
                if i%2:
                    position = [Window.size[0]/2 - self.platform_green_size[0], 150*i]
                    Color(1,1,1,1)
                    Rectangle(
                        source=self.platform_green_src,
                        pos=(position[0], position[1]), 
                        size=(self.platform_green_size[0], self.platform_green_size[1])
                    )
                    self.platforms_green_pos.append([position[0], position[1] + self.platform_green_size[1]])
                    
                    position = [Window.size[0]/2, 150*i]
                    Color(1,1,1,1)
                    Rectangle(
                        source=self.platform_green_src, 
                        pos=(position[0], position[1]), 
                        size=(self.platform_green_size[0], self.platform_green_size[1])
                    )
                    self.platforms_green_pos.append([position[0], position[1] + self.platform_green_size[1]])
                else:
                    position = [Window.size[0]/2 - self.platform_green_size[0]/2, 150*i]
                    Color(1,1,1,1)
                    Rectangle(
                        source=self.platform_green_src, 
                        pos=(position[0], position[1]), 
                        size=(self.platform_green_size[0], self.platform_green_size[1])
                    )
                    self.platforms_green_pos.append([position[0], position[1] + self.platform_green_size[1]])

        Clock.schedule_interval(self.update, 0.001)
        
    def update(self, *args):
        pass
        # for plat_pos in self.platforms_green_pos:
        #     if ((self.doodle.pos[1] - plat_pos[1]) < 1) and (self.doodle.pos[0] > plat_pos[0]) and (self.doodle.pos[0] < (plat_pos[0] + self.platform_green_size[0])):
        #         self.doodle.jump()