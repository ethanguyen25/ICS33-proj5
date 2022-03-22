# Black_Hole inherits from only Simulton, updating by finding+removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter
 
from simulton import Simulton
from prey import Prey
 
 
class Black_Hole(Simulton):
    radius = 10
     
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        self._color = "Black"
         
    def contains(self, object):
        """
        the distance from the center of the Black_Hole to the 
        center of the object is less than the radius of the Black_Hole
        """
        if isinstance(object, tuple):
            return Simulton.distance(self, object) < (self._width/2) #Black_Hole.radius
        else:
            return Simulton.distance(self, object.get_location()) < (self._width/2) #Black_Hole.radius
 
     
    def update(self, model):
        eaten = set()
        prey = model.find(lambda x: isinstance(x, Prey) == True)
        for x in prey:
            if self.contains(x):
                eaten.add(x)
        for y in eaten:
            model.remove(y)
#         if eaten != set():
#             print(eaten)
        return eaten
     
    def display(self,canvas):
        canvas.create_oval(self._x-(self._width/2), self._y-(self._height/2),
                          self._x+(self._width/2), self._y+(self._height/2),
                          fill = self._color)

            