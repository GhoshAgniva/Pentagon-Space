class Os:
    def __init__(self):
        self.status=True
        print("os is instaling")
    def getOs(self):
        print("OS is insatlling")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=Os()
        print("mobile is ready")
        print("With os imstalled")
m=Mobile("iphone")
print(m.mname)
print(m.o.status)
m.o.getOs()
# #if we delete m object then nothing will exicute
# del m
# print(m.mname)
# print(m.o.status)
