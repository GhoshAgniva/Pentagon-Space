#this is a normal program any one can access
# class Book:
#     def __init__(self,value):
#         self.page=value
# b1=Book(100)
# print(b1.page)

#Data encapsulation

class Book:
    def __init__(self,value):
        self.__page=value

    def setter(self,value):
        if value>0:
            self.__page=value
    def getter(self):
        return self.__page
b1=Book(100)
b1.setter(-99)
result=b1.getter()
print(result)

#Data encapsulation
class Student:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value
s1=Student()
s1.setter("Ram")
out=s1.getter()
print(out)