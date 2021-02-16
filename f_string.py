# string formatting
me ="Harry"
a1= 3
a= "this is %s %s" %(me, a1)
print(a)


a= "this is {1} {0}"
b= a.format(me, a1)
print(b)


# f string
import math
a= f"this is {me} {a1} {4*65} {math.cos(65)}"
print(a)