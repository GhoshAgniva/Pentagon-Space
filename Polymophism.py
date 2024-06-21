class Plane:
    def take_off(self):
        print("Plane is take off")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")

class Cargoplane(Plane):
    def take_off(self):
        print("Cargo plane is take of")
    def fly(self):
        print(" cargo plane is flying")
    def land(self):
        print("cargo plane is landing")
    def carry(self):
        print("plane carrying goods")

class Fighterplane(Plane):
    def take_off(self):
        print(" Fighter Plane is take off")
    def fly(self):
        print("Fighter plane is flying")
    def land(self):
        print("Fighter plane is landing")
    def carry(self):
        print(" fighter plane carrying weapons")

class Passengerplane(Plane):
    def take_off(self):
        print(" passenger Plane is take off")
    def fly(self):
        print("Passenger plane is flying")
    def land(self):
        print("Passenegr plane is landing")
    def carry(self):
        print("Passenger plane carrying Passengers")

c=Cargoplane()
p=Passengerplane()
f=Fighterplane()

def allow_plane(ref):
    ref.take_off()
    ref.fly()
    ref.land()
    ref.carry()

allow_plane(c)
allow_plane(p)


