# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random, randrange


class Floater(Prey): 
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,5)
        self.randomize_angle()
        self._color = "Red"
        
    def update(self,model):
        self.move()
        self.wall_bounce()
        
        if random() < .30:
            self._speed = self.get_speed() + (randrange(-5,5)/10)
            self._angle = self.get_angle() + (randrange(-5,5)/10)
            if self._speed < 3:
                self._speed = 3
            elif self._speed > 7:
                self._speed = 7
        elif random() >= .30:
            pass
        
    def display(self,canvas):
       canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                          self._x+Floater.radius, self._y+Floater.radius,
                          fill = self._color)
