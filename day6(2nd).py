#Methode returning multiple values
class Demo:
    def arth_op(self,x,y):
        s1=x+y
        s2=x-y
        s3=x*y
        s4=x/y
        return s1,s2,s3,s4
d1=Demo()
a=10
b=20
a1,a2,a3,a4=d1.arth_op(a,b)
print(a1)
print(a2)
print(a3)
print(a4)



