class phone:
    def __init__(self,mobile,battery):
        self.mobile = mobile
        self.battery = battery
    def use_phone(self):
        self.battery-=5
        print("model "+self.mobile+" has a battery off "+str(self.battery)+"%")
phone1 = phone("samsung",75)
phone2 = phone("apple",50)
phone1.use_phone()
phone2.use_phone()