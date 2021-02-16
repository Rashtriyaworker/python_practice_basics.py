# # tell and seek function
# f=open("reading.txt","rt")
# # f.read()
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readlines())
#f.close()


# f= open("reading.txt","r+")
# print(f.read())
# print(f.seek(10))
# #f.write("chlo sahi hai")
# print(f.read())
# f.close()

with open("reading.txt") as f:
    a= f.readlines()
    print("0-",a)

f= open("reading.txt")
print("1-",f.readlines())
f.close()