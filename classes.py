class vehicle:
    def __init__(self,tires,speed,motor,type):
        self.tires = tires
        self.speed = speed
        self.motor = motor
        self.type = type
    def p(self):
        print("tires"+self.tires)
        print("speed"+self.speed)
        print("motor"+self.motor)
        print("type"+self.type)
vehicle1 = vehicle(":thin",":10kph",":none",":bike")
vehicle2 = vehicle(":normal",":180kph max",":benzine motor",":car")
vehicle3 = vehicle(":normal","200kph max",":electric",":electric car")
vehicle1.p()
vehicle2.p()
vehicle3.p()
        