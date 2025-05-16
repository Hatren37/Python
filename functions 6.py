#function with variable length arguments
def fun1(*a):
   print(a)
   print(type(a))
fun1(10)
fun1(100, 200)
fun1(1,2,3,4,5,6,7,8,9)
fun1()