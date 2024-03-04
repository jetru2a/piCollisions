LEFT_POS = 100 
LEFT_MASS = 1
RIGHT_POS = 250
RIGHT_MASS = 100
RIGHT_SPEED = -1
RECT_WIDTH = 75

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
    def __init__(self):
        self.leftRect = Rect(LEFT_POS,LEFT_MASS,0)
        self.rightRect = Rect(RIGHT_POS,RIGHT_MASS,RIGHT_SPEED)
        self.rectWidth = RECT_WIDTH
        self.count = 0

    def changeMass(self, mass):
        self.rightRect.mass = mass

    def restart(self):
        self.leftRect.pos = LEFT_POS
        self.leftRect.speed = 0
        self.rightRect.pos = RIGHT_POS
        self.rightRect.speed = RIGHT_SPEED
        self.count = 0

    def simulate(self):
        precision = self.rightRect.mass
        timeLeft = precision
        while(timeLeft > 0):
            nextLeft = self.leftRect.pos + timeLeft*self.leftRect.speed/precision
            nextRight = self.rightRect.pos + timeLeft*self.rightRect.speed/precision
            if (nextLeft > 0 and nextLeft + self.rectWidth < nextRight):
                self.leftRect.pos, self.rightRect.pos = nextLeft, nextRight
                break
            timeUntilWallCollision = 0
            timeUntilRectCollision = 0
            if nextLeft < 0 and nextLeft + self.rectWidth > nextRight:
                timeUntilWallCollision = -self.leftRect.pos*precision/self.leftRect.speed
                timeUntilRectCollision = (self.rightRect.pos - self.leftRect.pos -self.rectWidth)/(self.leftRect.speed - self.rightRect.speed)*precision
                wallCollision = timeUntilWallCollision < timeUntilRectCollision
            else:
                wallCollision = nextLeft < 0
            if (wallCollision):
                    self.leftRect.pos = 0
                    self.leftRect.speed *= -1
                    self.count += 1
                    self.rightRect.pos += timeUntilWallCollision*self.rightRect.speed/precision
                    timeLeft -= timeUntilWallCollision
            else:
                self.leftRect.pos += timeUntilRectCollision*self.leftRect.speed/precision
                self.rightRect.pos += timeUntilRectCollision*self.rightRect.speed/precision
                self.leftRect.speed, self.rightRect.speed = collide(self.leftRect, self.rightRect)
                self.count += 1
                self.rightRect.pos = self.leftRect.pos + self.rectWidth
                timeLeft -= timeUntilRectCollision

        return self.leftRect.pos, self.rightRect.pos
    
    def estimation(self):
        return self.count / 10**(len(str(self.count))-1)
