list1= ["Bhindi", "Baigan", "chopstics","Aloo"]

# i=1
# for item in list1:
#     if i % 2 != 0:
#         print(f"bring these items {item}")
#     i= i+1

for index, item in enumerate(list1):
    if index%2==0:
        print(f"bring {item}")
