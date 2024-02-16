


class LeftRect:
    def __init__(self):
        self.mass = 1 #kg
        self.pos = 1 #m from left wall
        self.speed = 0 #m/s to the left

class RightRect:
    def __init__(self,mass):
        self.mass = mass #kg
        self.pos = 3 #m from left wall
        self.speed = 1 #m/s to the left

class Collisions:
    def __init__(self):
        self.leftRect = LeftRect()
        self.rightRect = RightRect(10)

    
    def changeMass(self, mass):
        self.rightRect.mass = mass

    