
from math import sqrt

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
    
    def __add__(self, b):
        return Vector(self.x + b.x, self.y + b.y)
    
    def __repr__(self):
        return "Vector({0},{1})".format(self.x, self.y)
    