class Plane:
    def take_off(self):
        print("Plane is take off")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")

class Cargoplane(Plane):
    def carryc(self):
        print("plane carrying goods")

class Fighterplane(Plane):
    def carryf(self):
        print("plane carrying weapons")

class Passengerplane(Plane):
    def carryp(self):
        print("plane carrying Passengers")

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
