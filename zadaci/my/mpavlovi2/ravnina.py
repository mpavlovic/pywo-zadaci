
from math import sqrt
import types

class Tocka(object):
    """
    Opis klase.
    2 - dim tocke u ravnini
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "Tocka({0},{1})".format(self.x, self.y)
    
    def norm(self):
        return sqrt(self.x**2 + self.y**2)

class Vector(Tocka):
    
    def __repr__(self):
        return "({0},{1})".format(self.x, self.y)
    
    def __add__(self, b):
        return Vector(self.x + b.x, self.y + b.y)
    
    def __sub__(self, b):
        return Vector(self.x - b.x, self.y - b.y)
    
    def __mul__(self, b):
        if isinstance(b, int):
            return Vector(self.x * b, self.y * b)
        elif isinstance(b, Vector):
            return self.x * b.x + self.y * b.y
        else:
            print("Operacija nije podrzana.")
            return 0
    
    def __rmul__(self, b):
        if isinstance(b, int):
            return Vector(self.x * b, self.y * b)
        elif isinstance(b, Vector):
            return self.x * b.x + self.y * b.y
        else:
            print("Operacija nije podrzana.")
            return 0
    