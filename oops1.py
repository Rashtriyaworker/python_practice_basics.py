class Students:
    no_of_subjects= 5
    pass

Harry= Students()
Larry= Students()

Harry.name="Harry"
Harry.age =19
Harry.subject=["Physics", "Chemistry", "English"]
Harry.Class= 12

Larry.name="Larry"
Larry.age =15
Larry.subject=["Science", "Hindi", "English"]
Larry.Class= 9

print(Larry.subject)
print(Harry.subject)

print(Harry.no_of_subjects)
Harry.no_of_subjects= 6
print(Harry.no_of_subjects)
print(Students.no_of_subjects)
print(Harry.__dict__)
print(Larry.__dict__)
Larry.no_of_subjects =4
print(Larry.__dict__)
print(Students.__dict__)
Students.no_of_subjects = 8
print(Students.__dict__)