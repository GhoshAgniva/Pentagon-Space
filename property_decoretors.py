class Student:
    def __init__(self):
        self.__name=""

    @property
    def dataAccess(self):
        return self.__name
    @dataAccess.setter
    def dataAccess(self,value):
        self.__name=value
        return value

p1=Student()
p1.dataAccess="Ram"
result=p1.dataAccess
print(result)
