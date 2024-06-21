# #single threded program
# import time
# class Demo:
#     def printNames(self):
#         names=["ram","sita","ravan"]
#         for i in names:
#             print(i)
#             time.sleep(4)
#
#     def printNum(self):
#         for i in range(10):
#             print(i)
#             time.sleep(2)
#
#     def add(self):
#         a=10
#         b=20
#         z=a+b
#         print("sum is: ",z)
#
# d=Demo()
# d.printNames()
# d.printNum()
# d.add()

class Number:
    def even(self):
        for i in range(100):
            if i%2==0 or i!=0:
                print(i)
    def odd(self):
        pass
n=Number()
n.even()
n.odd()
