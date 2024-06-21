class Student:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value
    getset=property(getter,setter)
s1=Student()
s1.getset="Rama" #
res=s1.getset
print(res)