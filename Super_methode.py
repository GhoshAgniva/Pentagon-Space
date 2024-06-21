#Invoking parents class constructor Manullay
class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        super().__init__()
        self.b=20
class C(B):
    def __init__(self):
        super().__init__()
        self.c1=30
cf=C()
print(cf.c1)
print(cf.b)
print(cf.a)