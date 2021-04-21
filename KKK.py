class Hand:
    def __init__(self,size):
        self.size=size
class Body:
    def __init__(self,capacity):
        self.capacity=capacity

class Leg:
    def __init__(self,width):
        self.width=width

class People:
    def __init__(self):
        self.hd=None
        self.bd=None
        self.rh=None
        self.Lh=None
        self.rl=None
        self.ll=None

a=People()
a.hd=Hand(20)
a.bd=Body(5000)
a.rh=Hand(30)
a.lh=Hand(30)
a.rl=Leg(80)
a.ll=Leg(80)
print(a.hd.size)



b=People()
b.hd=Hand(15)
b.bd=Body(3000)
b.rh=Hand(40)
b.lh=Hand(40)
b.rl=Leg(90)
b.ll=Leg(90)


