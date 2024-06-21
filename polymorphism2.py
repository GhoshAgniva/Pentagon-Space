class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleepinng")

    def breath(self):
        print("Animal is breathing")

class Tiger(Animal):
    def eat(self):
        print("Tiger  will hunt and eat")
    def sleep(self):
        print("Tiger is sleepinng")

    def breath(self):
        print("Tiger is breathing")

class Deer(Animal):
    def eat(self):
        print("deer  will grease and eat")
    def sleep(self):
        print("Deer is sleepinng")

    def breath(self):
        print("Deer is breathing")
class Monkey(Animal):
    def eat(self):
        print("monkey  will stole and eat")
    def sleep(self):
        print("monkey is sleepinng")

    def breath(self):
        print("monkey is breathing")

t=Tiger()
d=Deer()
m=Monkey()

def allow_animal(ref):
    ref.eat()
    ref.sleep()
    ref.breath()

allow_animal(t)
allow_animal(d)





