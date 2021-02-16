#----------------------*-----------------------------assigning a function into another function
#
# def func1():
#     print("okk run this function")
#
#
# func2 =func1
# del func1
# func2()

# ------------------------*----------------------------- returning a function inside a function
# def funct1(arg1):
#     if arg1==0:
#         return print
#     if arg1==1:
#         return int
#
# a= funct1(1)
# print(a)

# -------------------------*----------------------------execute a function inside function as an argument
# def executer(func1):
#     func1("this is a function")
#
# executer(print)

#----------------------------*-------------------------using decoators '@'

def dec1(func1):
    def executer():
        print("executing")
        func1()
        print("executed")
    return executer

@dec1
def func_of_Harry():
    print("Harry is a good boy")

# func_of_Harry= dec1(func_of_Harry)   # works as a decorator
func_of_Harry()


