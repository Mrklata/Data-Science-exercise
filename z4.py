import numpy


def list_creator():
    count = int(input("Insert number of elements"))
    nums = []
    for i in range(count):
        a = int(input("insert number"))
        nums.append(a)
    average = sum(nums) / len(nums)
    return nums, average


def user():
    nums, average = list_creator()
    deviation = 0
    for i in range(len(nums)):
        deviation += (int(nums[i]) - average) ** 2
    deviation = (deviation / len(nums)) ** (1/2)
    return deviation, average


def library():
    nums, average = list_creator()
    deviation = numpy.std(nums)
    return deviation, average


print(user())
print(library())
