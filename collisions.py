LEFT_POS = 1 
LEFT_MASS = 1
RIGHT_POS = 3
RIGHT_MASS = 10
RIGHT_SPEED = 1

def collide(leftRect, rightRect):
    leftMass, leftSpeed = leftRect.mass, leftSpeed
    rightMass, rightSpeed = rightRect.mass, rightRect.speed

    leftFinalSpeed = (leftMass - rightMass)/(leftMass+rightMass)*leftSpeed + 2*rightMass/(leftMass+rightMass)*rightSpeed
    rightFinalSpeed = (rightMass - leftMass)/(leftMass+rightMass)*rightSpeed + 2*leftMass/(leftMass+rightMass)*leftSpeed
    return (leftFinalSpeed,rightFinalSpeed)

class Rect:
    def __init__(self, pos, mass, speed):
        self.pos = pos
        self.mass = mass
        self.speed = speed

class Collisions:
    def __init__(self):
        self.leftRect = Rect(LEFT_POS,LEFT_MASS,0)
        self.rightRect = Rect(RIGHT_POS,RIGHT_MASS,RIGHT_SPEED)

    def changeMass(self, mass):
        self.rightRect.mass = mass

    def restart(self):
        self.leftRect.pos = LEFT_POS
        self.leftRect.speed = 0
        self.rightRect.pos = RIGHT_POS
        self.rightRect.speed = RIGHT_SPEED
    
    def animate(self,speed):
        self.leftRect.pos += self.leftRect.speed/10
        self.rightRect.pos += self.rightRect.speed/10
        if(self.leftRect.pos >= self.rightRect.pos):
            self.leftRect.speed, self.rightRect.speed = collide(self.leftRect, self.rightRect)
        if(self.leftRect.pos <= 0):
            self.leftRect.pos = 0
            self.leftRect.speed *= -1
        return self.leftRect.pos, self.rightRect.pos