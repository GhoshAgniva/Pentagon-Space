# #single threded program
import time
from threading import Thread
# class Task1(Thread):
#     def run (self):
#         names=["ram","sita","ravan"]
#         for i in names:
#             print(i)
#             time.sleep(4)
#
# class Task2(Thread):
#
#     def run (self):
#         for i in range(10):
#             print(i)
#             time.sleep(2)
# class Task3(Thread):
#     def run (self):
#         a=10
#         b=20
#         z=a+b
#         print("sum is: ",z)
#
# t1=Task1()
# t2=Task2()
# t3=Task3()
# t1.start()
# t2.start()
# t3.start()

#Example of multithreading
#printing even and odd number
class even(Thread):
    def run(self):
        for i in range(100):
            if i%2==0:
                print(i)
                time.sleep(2)

class odd(Thread):
    def run(self):
        for i in range(100):
            if i%2!=0:
                print(i)
                time.sleep(2)

e=even()
o=odd()
e.start()
o.start()
