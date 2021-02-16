# nums = [4,6,2,9]
# it = iter(nums)
# print(it.__next__())
# print(it.__next__())
# print(next(it))
# for i in nums:
#     print(i)
class Toptan():

    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num +=1
            return val

        else:
            raise StopIteration

values = Toptan()
print(next(values))
print(next(values))

for i in values :
    print(" this is", i)