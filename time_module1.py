import time
initial_time1= time.time()
for i in range(10):
    print("in for loop")
print(f"for loop mai {initial_time1-time.time()} hai \n\n")

x= 0
initial_time2 = time.time()
while x<10:
    time.sleep(1)
    print("in while loop")
    x+=1
print(f"while loop mai {initial_time2-time.time()} hai")


print(type({"gun":"go", "pistol": "fire"}))
print(type(time.localtime()))
local_time= time.asctime(time.localtime(time.time()))
print(local_time)