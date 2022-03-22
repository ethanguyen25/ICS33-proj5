# Hunter inherits from the Pulsator (1st) and Mobile_Simulton (2nd) classes:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    distance = 200
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,20,20,0,5)
        self.randomize_angle()
        self._color = "Black"
    
    def update(self, model):
        self.move()
        self.wall_bounce()
        eaten = Pulsator.update(self, model)

        lis = model.find(lambda x: isinstance(x, Prey) == True and Mobile_Simulton.distance(self,x.get_location()) <= Hunter.distance)
        potentials = [(Mobile_Simulton.distance(self,x.get_location()), x.get_location()) for x in lis]
#         potentials = {Mobile_Simulton.distance(self,y.get_location()) : y.get_location() for y in lis}
        if len(potentials) != 0:
#             print("P", potentials)
            target = min(potentials)
            x_coord = target[1][0] - self.get_location()[0]
            y_coord = target[1][1] - self.get_location()[1]
            self.set_angle(atan2(y_coord, x_coord))
        
        
        
    
