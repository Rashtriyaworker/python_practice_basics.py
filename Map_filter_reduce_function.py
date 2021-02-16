# map function
#
# numbers= ["3", "87", "6"]
#
# # for i in range(len(numbers)):
#      # numbers[i]= int(numbers[i])
# numbers1= list(map(int, numbers))
# print(numbers, numbers1)
# # numbers[2]= numbers[2]+1
# numbers1[2]= numbers1[2]+1
# print(numbers1[2])
#
# num = [9, 7, 10, 50, 8, 774]
#
#
# def square(x):
#     return x * x
#
#
# def cube(x):
#     return x * x * x
#
#
# list1 = [square, cube]
#
#
# for n in num:
#     number = list(map(lambda y: y(n), list1))
#     print(number)
#

# ----------------filter function----------------

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 50]
#
# # def func(i):
# #     return i>5
#
# val= list(filter(lambda i: i>5, list1))
# print(val)


# ------------------reduce function-------------------

list1 = [1, 2, 3, 4, 10]
# num= 0
# for i in list1:
#     num= num+i
#     print(num)
# print(num)
from functools import reduce
num = (reduce(lambda x,y: x+y, list1))
print(num)  