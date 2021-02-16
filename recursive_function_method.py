# factorial of a number from iterative method


# def print2(n):
#     fact = 1
#     for i in range(n):
#
#         fact = fact*(i+1)
#     return fact
#
#
# no = int(input("enter no to calculate factorial\n"))
# print("factorial of", no, "is", print2(no))

# factorial of a number from recursive method


def print2(n):
    if n == 1:
        return 1
    else:
         return n* (print2(n-1))

no = int(input("enter no to calculate factorial\n"))
print("factorial of", no, "is", print2(no))

