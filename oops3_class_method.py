class management:
    no_of_leaves= 8
    def __init__(self, name1, age1, salary1):
        self.name= name1
        self.age= age1
        self.salary= salary1

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves= new_leaves



Harry= management("Harry", 25, 45000)
Rohan= management("Rohan", 27, 60000)

# Harry.name= "Harry"
# Harry.age= 25
# Harry.salary= 45000
#
# Rohan.name= "Rohan"
# Rohan.age= 27
# Rohan.salary=60000
Rohan.no_of_leaves = 12
print(Rohan.no_of_leaves)
print(management.no_of_leaves)
Rohan.change_leaves(55)
print(management.no_of_leaves)