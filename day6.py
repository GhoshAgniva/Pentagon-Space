#Default argument and Keyword Argument
class Demo:
    def disp(self,x=11,y=22,z=33):
        print(x)
        print(y)
        print(z)
d1=Demo()
a=10
b=20
c=30
d1.disp(a,b,c)
d1.disp(x=a,y=b,z=c)
d1.disp(c)
d1.disp(a)
d1.disp()