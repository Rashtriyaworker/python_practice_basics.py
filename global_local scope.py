# x= 10
#
# def function1(n):
#     x= 7
#     print(n, "i have printed")
#     print(x, "in local")
# function1("this is the thing")
# print(x,"in global")

# x= 10
#
# def function1(n):
#     x= 7
#     x+=50
#     print(n, "i have printed")
#     # print(x, "in local")
# function1("this is the thing")
# print(x,"in global")


# x=10
# def function1(n):
#     global x
#     x+=50
#     print(n, "i have printed")
#     print(x, "in local")
# function1("this is the thing")
# print(x,"in global")


def function1(n):
    x= 5
    def function2(n):
        global x
        x= 88
        print(n)
        print(x,"in fun1 local")
    function2("in nested function")
    print(x,"in fun2 local")

function1("this is the thing")
print(x,"in global")