LEFT_POS = 100 
LEFT_MASS = 1
RIGHT_POS = 250
RIGHT_MASS = 10000
RIGHT_SPEED = -1

def collide(leftRect, rightRect):
    leftMass, leftSpeed = leftRect.mass, leftRect.speed
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
    def __init__(self, rectWidth):
        self.leftRect = Rect(LEFT_POS,LEFT_MASS,0)
        self.rightRect = Rect(RIGHT_POS,RIGHT_MASS,RIGHT_SPEED)
        self.rectWidth = rectWidth
        self.estimation = 0

    def changeMass(self, mass):
        self.rightRect.mass = mass

    def restart(self):
        self.leftRect.pos = LEFT_POS
        self.leftRect.speed = 0
        self.rightRect.pos = RIGHT_POS
        self.rightRect.speed = RIGHT_SPEED
    
    def animate(self):
        precision = self.rightRect.mass

        nextLeft = self.leftRect.pos + self.leftRect.speed
        nextRight = self.rightRect.pos + self.rightRect.speed
        if (nextLeft < 0 or nextLeft + self.rectWidth >= nextRight):
            for i in range(precision):
                self.leftRect.pos += self.leftRect.speed/precision
                self.rightRect.pos += self.rightRect.speed/precision
                if(self.leftRect.pos + self.rectWidth >= self.rightRect.pos):
                    self.leftRect.speed, self.rightRect.speed = collide(self.leftRect, self.rightRect)
                    self.estimation += 1
                    self.rightRect.pos = self.leftRect.pos + self.rectWidth
                if(self.leftRect.pos <= 0):
                    self.leftRect.pos = 0
                    self.leftRect.speed *= -1
                    self.estimation += 1
        else :
            self.leftRect.pos, self.rightRect.pos = nextLeft, nextRight
        return self.leftRect.pos, self.rightRect.pos
