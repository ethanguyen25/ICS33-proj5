# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter = 30
    
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._counter = 0
        self._color = "Black"
        
    def update(self, model):
        eaten = Black_Hole.update(self, model)
        self._counter += 1
#         if self._counter % 10 == 0:
#             print("COUNT",self._counter)
        if len(eaten) == 0:
            if self._counter == Pulsator.counter:
#                 print(self._width, self._height)
                self.change_dimension(-1,-1) 
                self._counter = 0
                if self._width == 0 and self._height == 0:
                    model.remove(self)
                    self._counter = 0
#             self._counter = 0
        else:
            self._counter = 0
            self.change_dimension(+1,+1)
        return eaten

            
            
        
        
        
        
    
