class Cargoplane:
    def take_off(self):
        print("Plane is take off")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
    def carryc(self):
        print("Plane is carrying goods")

class Passengerplane:
    def take_off(self):
        print("Plane is take off")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
    def carryp(self):
        print("Plane is carrying passengers")

class Fighterplane:
    def take_off(self):
        print("Plane is take off")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
    def carryf(self):
        print("Plane is carrying weapons")

c=Cargoplane()
p=Passengerplane()
f=Fighterplane()

c.take_off()
c.fly()
c.land()
c.carryc()

p.take_off()
p.fly()
p.land()
p.carryp()

f.take_off()
f.fly()
f.land()
f.carryf()

