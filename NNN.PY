class Person:
    def __init__(self,name,weight,hp,ap):
        self.name=name
        self.weight=weight
        self.hp=hp
        self.ap=ap
    
    def eat(self,volume):
        self.weight=self.weight+volume

    def exercie(self):
        self.weight=self.weight-1
    def underattack(self,who):
        self.hp=self.hp-who.ap



a=Person("NNN",95,2000,150)
print(a.weight)
a.eat(10)
print(a)
print(a.name)
print(a.weight)

b=Person("aaa",60,1000,75)

print(b)
print(b.name)
print(b.weight)
b.exercie()
print(b.weight)

print(a.hp)
a.underattack(b)
print(a.hp)

print(b.hp)
b.underattack(a)
print(b.hp)
