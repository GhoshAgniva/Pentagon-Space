class Student:
    def __init__(self):
        self.__name=""

#public
    def dataAccess(self):
        print("python")
#private
    def __dataAccess1(self):
        print("program")

    def dataAccess2(self):
        self.__dataAccess1()

#protected
    def __dataAccess3(self):
        print("data")
    def dataAccess4(self):
        self.__dataAccess3()


s1=Student()
s1.dataAccess()
s1.dataAccess2()
s1.dataAccess4()