with open("reading.txt","r+") as f:
    print( f.write("just go and complete it"))

f= open("reading.txt","r+")
#print(f.read())
#print(f.write("yes do your work in time pankaj singh khani"))
#print(f.write("yes now you can add more text"))
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# print("1",f.read())
# print(f.tell())
print(f.readlines())
print(f.tell())

print(f.seek(0))
#print(f.write("yes you are able to do it\n"))
print(f.tell())

f.close()