# ----------------------------------defining class and object------------------------------------------------

# class computer:                                     # class defining
#
#
#     def config(self):                               # defining a method
#         print("config is" )
#
# com1= computer()                                    # defining object
# com2= computer()                                    # defining object
#
# print("1", "defining class and object")
# computer.config(com1)                               # calling a function or method
# com1.config()                                       # calling a function or method
#

# # ------------------------------------defining __init__ method----------------------------------------------------
# class computer:
#
#     def __init__(self, ccpu, cram):                  # defining init method   or a constructor
#         self.cpu= ccpu                               # instance variable
#         self.ram= cram                               # instance variable
#
#
#     def config(self):
#         print("config is ", self.cpu, self.ram)
#
#
#
# com1= computer("i5", "16GB")
# com2= computer("Ryzen 3", "8GB")
#
# com1.config()
# com2.config()


# ------------------------------------constructor, self and comparing objects--------------------------------------

#
# class computer:
#
#     def __init__(self):                            # a constructor
#         self.name="Pankaj"
#         self.age= 26
#
#     def update(self):                               # a constructor
#         self.name= "Madan"
#         self.age= 27
#
# com1= computer()
# com2= computer()
#
# com1.update()
# com2.update()
# com2.name= "Suresh"
# com2.age= "30"
# print(com1.name, com1.age)
# print(com2.name, com2.age)
#

# ##comparing objects

# class computer:
#
#     def __init__(self):
#         self.name= "Pankaj"
#         self.age= 26
#
#     def compare(self, other):                      # comparing through methods
#         if self.age== other.age:
#             return True
#         else:
#             False
#
# c1= computer()
# c2= computer()
# # print(type(c1))
#
# c2.name= "Suresh"
# c2.age= 30
# if c1.compare(c2):                                   # comparing objects
#     print("They are same")
#
# else:
#     print("They are different")


# ---------------------------------------types of variables in python--------------------------------------------------
# instance variable and class or static variable
# class car:
#     wheel= 4                                         # class variable
#
#
#     def __init__(self):
#         self.com= "BMW"                            # instance variable
#         self.mil= 15                               # instance variable
#
# c1= car()
# c2= car()
# c1.com= "Hyundai"
# c1.mil= 20
#
# car.wheel= 5                                      # updating class variable
#
# c1.wheel= 4                                       # changing instance variable for object 1
#
# print(c1.com, c1.mil, c1.wheel)
# print(c2.com, c2.mil, c2.wheel)
#
#

# -----------------------------------------Types of methods in python-----------------------------------------------

# #  Instance method
#
# class student:
#
#
#     def __init__(self, m1, m2,m3):
#         self.r1= m1
#         self.r2= m2
#         self.r3= m3
#
#     def avg(self):                                               # instance method as working with instance variable
#         return (self.r1+self.r2+self.r3)/3                       # takes arguments as self
#
#
# s1= student(23, 24, 91)
# s2= student(87, 71, 45)
#
# print(s1.avg())
# print(s2.avg())


# # accessors or getters and mutators or setters in instance method in python
#
# class student:
#
#
#     def __init__(self, m1, m2,m3):
#         self.m1= m1
#         self.m2= m2
#         self.m3= m3
#
#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
#
#     def get_m1(self):                                        # accessors or getters
#         return self.m1

#     def set_m1(self,value):                                  # mutators or setters
#         self.m1= value
#         return self.m1
#
# s1= student(23, 24, 91)
# s2= student(87, 71, 45)

# print(s1.avg())
# print(s2.avg())
#
# print(s1.get_m1())                                            # calling accessors
# print(s2.get_m1())
#
# print(s1.set_m1(5))                                           # calling mutators



# # class methods
#
# class student:
#     school= "Telusko"                                    # class variable
#
#     def __init__(self, m1, m2,m3):
#         self.m1= m1
#         self.m2= m2
#         self.m3= m3
#
#     @classmethod                                         # decorator
#     def school_details(cls):                             # class method as working with class takes argument as cls
#         return cls.school
#
#
#
# s1= student(23, 24, 91)
# s2= student(87, 71, 45)
#
# print(student.school_details())                          # calling class method


# # static method

# class student:
#
#     def __init__(self, m1, m2,m3):
#         self.m1= m1
#         self.m2= m2
#         self.m3= m3
#
#     @staticmethod                                                      # decorator
#     def info():                                                        # defining static method takes no arguments
#         print('this is student class static method')
#
#
#
# s1= student(23, 24, 91)
# s2= student(87, 71, 45)
#
# student.info()                                                       # calling static method

#-------------------------------------inner class or nested class--------------------------------------------------

# class student:
#
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno= rollno
#         self.l1= self.laptop("HP","i5",'8GB')                                 # defining inner object inside outer class
#         self.l2= self.laptop("lenevo", "i7", '4GB')                           # defining inner object inside outer class
#
#
#     def show(self):
#         print(self.name, self.rollno)
#         self.l1.show1()                                                        # calling inner method inside outer class
#         self.l2.show1()                                                        # calling inner method inside outer class
#
#
#     class laptop:
#
#         def __init__(self, brand, cpu, ram):
#
#             self.brand = brand
#             self.cpu = cpu
#             self.ram= ram
#
#         def show1(self):
#             print(self.brand, self.cpu, self.ram)
#
#
# s1= student("Nitin", 2 )
# s2 =student("Jenny", 3)
# s1.show()
# s2.show()

# l1= s1.laptop("HP","i5")                                # defining inner object outside outer class
# l2= s2.laptop("lenevo", "i7")                           # defining inner object outside outer class
# l1.show1()                                              # calling inner method outside outer class
# l2.show1()                                              # calling inner method outside outer class

## -------------------------------------constructor in inheritence------------------------------------------------

#
# class A:
#     def __init__(self):
#         print("in A init")
#
#     def feature1(self):
#         print("feature1 is working")
#
#     def feature2(self):
#         print("feature2 is working")
#
# class B(A):
#     # def __init__(self):
#     #     super().__init__()
#     #     print("in B init")
#
#     def feature3(self):
#         print("feature3 is working")
#
#     def feature4(self):
#         print("feature4 is working")
#
#
#
# a1= B()
# a1.feature2()


#
# class A:
#     def __init__(self):
#         print("in A init")
#
#         print("feature1 is working")
#
#     def feature2(self):
#         print("feature2 is working")
#
# class B:
#     def __init__(self):
#         super().__init__()
#         print("in B init")
#
#     def feature3(self):
#         print("feature3 is working")
#
#     def feature4(self):
#         print("feature4 is working")
#
#
# class C(A,B):
#     def
# a1= B()

# ------------------------------------polymorphism in Python-------------------------------------------
# 4 ways
# 1- Duck typing
# 2- operator overloading
# 3- method overloading
# 4- operator overriding

# ------------------------------------------------1- Duck typing-----------------------------------------------
# class myeditor:
#     def execute(self):
#         print("spell check")
#         print("convention check")
#         print("compiling")
#         print("running")


# class PyCharm:
#     def execute(self):
#         print("compiling")
#         print("running")
#
#
# class laptop:
#     def code(self, ide):
#         ide.execute()
#
#
# # ide = PyCharm()
# ide = myeditor()
# lap1 = laptop()
# lap1.code(ide)

#     def feature1(self):


# ------------------------------------2 operator overloading-------------------------------------------------
#
# a= 5
# b = 8
# d= 'Navin'
# c = a+b
# print(c)
# print(int.__add__(a,b))
#
# print(a+d)

# class student:
# s3 = student(s1,s2)
#     def __init__(self, m1, m2):
#         self.m1= m1
#         self.m2= m2
#
#     def __add__(self, other):
#         r1= self.m1+ other.m1
#         r2= self.m2+other.m2
#         s3 = student(r1,r2)
#         return s3
#
#
#
# s1= student(53,97)
# s2= student(87,48)
# s3= s1+s2
# print(s3.m1)
#
# class student :
#     def __init__(self, m1, m2):
#         self.p1= m1
#         self.m2= m2
#
#     def __add__(self, other):
#         r1 = self.p1+ other.p1
#         r2 = self.m2 + other.m2
#         s3 = student(r1,r2)
#         return s3
#
#     def __gt__(self, other):
#         r1= self.p1+self.m2
#         r2= other.p1+other.m2
#         if r1>r2:
#             return True
#         else:
#             return False
#     # def __str__(self):
#     #     return self.p1, self.m2
#     def __str__(self):
#         return '{} {}'.format(self.p1, self.m2)
#
# s1 = student(25, 97)
# s2 = student(549,32)
#
# s3 = s1+s2
# print(s3.p1)
#
# if s1>s2:
#     print("s1 wins")
# else:
#     print("s2 wins")
#
# a=9
# print(a.__str__())
#
# print(s1.__str__())
# print(s1)


# -----------------------------------3 Method overloading-----------------------------------------------------
#
# class student:
#     def __init__(self,m1, m2):
#         self.m1= m1
#         self.m2= m2
#
#     def sum(self,a= None, b= None, c= None ):
#         if a!= None and b!=None and c!=None:
#             sum = a+b+c
#             print(sum)
#         elif a!= None and b!= None:
#             sum = a+b
#             print(sum)
#         else:
#             sum= a
#             print(sum)
#
#
# s1 = student(59,64)
# s1.sum(7,9)


#-------------------------------------------4 method overriding-------------------------------------------

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

o1 = B()
o1.show()



# -------------------------something codede--------------------------------------------------------------
class PyCharm:
    def execute(self):
        print("compiling")
        print("running")


class laptop:
    def code(self, ide1):
        print("its working")
        ide1.execute()


ide1 = PyCharm()
lap1 = laptop()
lap1.code(ide1)