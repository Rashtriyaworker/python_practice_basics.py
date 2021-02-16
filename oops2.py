# ------------------Shelf as an argument of a function------------------
'''class management:
    def function1(self):
        return f"name is {self.name}, age is {self.age} and salary is {self.salary}"

Harry= management()
Rohan= management()

Harry.name= "Harry"
Harry.age= 25
Harry.salary= 45000

Rohan.name= "Rohan"
Rohan.age= 27
Rohan.salary=60000

print(Harry.function1())
'''
#-----------------__init__ constructors------------------------
class management:
    def __init__(self, name1, age1, salary1):
        self.name= name1
        self.age= age1
        self.salary= salary1



Harry= management("Harry", 25, 45000)
Rohan= management("Rohan", 27, 60000)

# Harry.name= "Harry"
# Harry.age= 25
# Harry.salary= 45000
#
# Rohan.name= "Rohan"
# Rohan.age= 27
# Rohan.salary=60000

print(Harry.name,"\n", Harry.salary, "\n", Harry.age,"\n\n\n",Rohan.name,"\n", Rohan.salary,"\n", Rohan.age)



