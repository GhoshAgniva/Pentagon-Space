def fun1():
    #non local variable
    a=10
    print(a)
    def fun2():
        b = 20
        print(a)
        print(b)

    fun2()
    print(a)


fun1()
#example2
def fun3():
    a=10
    b=20
    print(a)
    print(b)
    def fun4():
        a=100
        c=30
        print(a)
        print(c)
    print(a)
    fun4()
    print(a)
fun3()