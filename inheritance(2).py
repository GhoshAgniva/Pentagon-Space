#creating a object in a derived class or child class
class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        A.__init__(self)
        self.b=20
class C(B):
    def __init__(self):
        B.__init__(self)
        self.c=30
cf=C()
print(cf.a)
print(cf.b)
print(cf.c)