#composed
class Heart:
    def __init__(self,name):
        self.hname=name
        print("heart is ready")
    def getHeart(self):
        print("heart is ok")

#Aggrigate
class Car:
    def __init__(self,name):
        self.cname=name
    def getcar(self):
        print("person have a car")

#main Class
class Person:
    def __init__(self,name):
        self.pname=name
        self.h=Heart("blood")
        self.c1=""
        print("person is ready")
    def hasPerson(self,c):
        self.c1=c
        print("person is driving")
p=Person("Ram")
c=Car("Lord Alto")
p.hasPerson(c)
print(p.pname)
print(p.h.hname)
print(p.c1.cname)
p.h.getHeart()
del p
print(c.cname)
c.getcar()

