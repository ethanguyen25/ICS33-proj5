
from prey import Prey
from mobilesimulton import Mobile_Simulton
from math import atan2

"""
This special class makes rectangular objects whose purpose is to feed itself to 
    Pulsator's and Hunters when they hit a certain dimension (between 15 and 20).
    In this window, the specials (if in range), will go directly to Pulsator's and
    Hunters so that they are given more chances to survive a little longer.
Their purpose is to serve Pulsator's and Hunters, hence why they are Prey.
"""



class Special(Prey, Mobile_Simulton):
    distance = 300
    
    def __init__(self,x,y):
        Mobile_Simulton.__init__(self,x,y,3,3,0,20)
#         self.randomize_angle()
        self._color = "Green"
        
    
    def update(self, model):
        friends = model.find(lambda x: not isinstance(x, (Special, Prey)) and Mobile_Simulton.distance(self,x.get_location()) <= Special.distance)
        l = [(Mobile_Simulton.distance(self,x.get_location()), x.get_location(), x) for x in friends]
        if len(l) != 0:
            target = min(l)
#             print(target)
#             print(target[2])
#             print(target[2].get_dimension())
            if (15,15) <= (target[2].get_dimension()) < (20,20):
                print(target[2].get_dimension())
                x_coord = target[1][0] - self.get_location()[0]
                y_coord = target[1][1] - self.get_location()[1]
                self.set_angle(atan2(y_coord, x_coord))
                self.move()
                self.wall_bounce()
            
    def display(self,canvas):
        canvas.create_rectangle(self._x-(self._width), self._y-(self._height),
                           self._x+(self._width), self._y+(self._height),
                           fill=self._color)
            
             
