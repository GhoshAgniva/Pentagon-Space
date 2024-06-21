class A:
    def display(self):
        print("inside A")
class B(A):
     def display(self):
        print("inside B")
class C(B):

    def display(self):
        print("inside C")

class D(C):
    def displayd(self):
        print("inside D")
        A.display(self)
        B.display(self)
        C.display(self)

d1=D()
d1.displayd()






