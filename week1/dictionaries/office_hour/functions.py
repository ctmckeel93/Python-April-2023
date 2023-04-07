# syntax
import random

nums = []
for i in range(11):
    nums.append(random.randint(1,101))
print(nums)

def sum_array(num_list):
    sum = 0
    for num in num_list:
        sum+=num
    return sum


def avg(num_list):
    return sum_array(num_list)/len(num_list)

list_avg = round(avg(nums), 2)

print(list_avg)