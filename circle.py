import math
class Circle:
    def __init__(self,radius):
      self.radius=radius
    
    def area(self):
       return 3.14*( self.radius**2)
    def circumference(self):
        return 2*3.14*self.radius
c1=Circle(5)
print(c1.area())
print(c1.circumference())

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Calculate and return the area of the circle
        return math.pi * self.radius ** 2