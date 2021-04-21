class Engine:
    def __init__(self):
        self.power=power
class Body:
    def __init__(self,capacity):
        self.capacity=capacity

class Wheel:
    def __init__(self,size):
        self.size=size

class Car:
    def __init__(self):
        self.pw=None
        self.bd=None
        self.brw=None
        self.blw=None
        self.arw=None
        self.alw=None

a=Car()
a.pw=Engine(50000)
a.bd=Body(5000)
a.brw=Wheel(40)
a.blw=Wheel(40)
a.arw=Wheel(40)
a.alw=Wheel(40)