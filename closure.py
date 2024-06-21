def fun1():
    print("hi all")
    def fun2():
        print("inside fun2")
    return fun2
ptr1=fun1()
print(ptr1)
ptr1()
