f = open("writing.txt","r+")
p=f.read()

f.write("\nthis is me\n")
print(p)
print(f.write("okk come in"))
f.close()