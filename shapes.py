class shapes:
    def __init__(self,color,size,sides):
        self.color = color
        self.size = size
        self.sides = sides
    def f(self):
        print("color"+self.color)
        print("size"+self.size)
        print("sides"+self.sides)
shape1 = shapes(":red",":10",":0")
shape2 = shapes(":blue",":5",":8")
shape3 = shapes(":yellow",":3",":4")
shape1.f()
shape2.f()
shape3.f()