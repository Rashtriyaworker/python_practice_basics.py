def test_args_and_kwargs(normal, *args1, **kwargs1):
    print(args1)   # pass the list or tuple as tuple in function
    print(args1[0])
    print(normal)
    for item in args1:
        print(item)

    for key1, value1 in kwargs1.items():
        print(f"{key1} is a {value1}")

run_dict= {"Harry":"programmer", "rohan":"fitness coach"}
nor1= "he is a good boy"
names = ["Harry", "rohan", "maya", "Gunner"]
test_args_and_kwargs(nor1, *names, **run_dict)