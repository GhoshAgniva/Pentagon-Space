class Parent:
    def __init__(self):
        self.a=10

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.b=30

p1=Child()
print(p1.b)
print(p1.a)