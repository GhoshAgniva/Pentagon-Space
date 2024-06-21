#LEGB rule

x=10
def fun1():
    x=15
    def fun2():
        x=20
        print(x)
    fun2()
fun1()

