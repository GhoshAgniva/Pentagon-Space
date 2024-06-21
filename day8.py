a=10
def outer():
    global a
    a=100
    b=20
    print(a)
    print(b)
    def inner():
        nonlocal b
        b=200
        c=30
        print(a)
        print(b)
        print(c)
    inner()
outer()
class Demo:
    x=40
    def _init_(self):
        self.y=50
        self.z=60
    def disp(self):
        print(self.z)
        self.z1=70
        y1=80
        print(y1)
d1=Demo()
d1.disp()
print(Demo.x)
print(d1.y)