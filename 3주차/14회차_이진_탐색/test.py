import copy
import random
import time

n1 = 1000000
shop1 = random.sample(range(1,1000001),1000000)
m1 = 500000
customer1 = random.sample(range(1,500001),500000)

shop2 = copy.deepcopy(shop1)
customer2 = copy.deepcopy(customer1)

shop3 = copy.deepcopy(shop1)
customer3 = copy.deepcopy(customer1)


def binary_search(nums, target):
    def bs(start, end):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] < target:
            return bs(mid + 1, end)
        elif nums[mid] > target:
            return bs(start, mid - 1)
        else:
            return mid

    return bs(0, len(nums) - 1)

# 1
start_time1 = time.process_time()
shop1.sort()
for i in customer1:
    result = binary_search(shop1, i)
    if result != None:
        pass
    else:
        pass
end_time1 = time.process_time()
print(f"작동시간1 : {end_time1 - start_time1}")

# 2
start_time2 = time.process_time()
array2 = [0] * 1000001

for i in shop2:
    array2[int(i)] = 1

for i in customer2:
    if array2[i] == 1:
        pass
    else:
        pass

end_time2 = time.process_time()
print(f"작동시간2 : {end_time2 - start_time2}")
# 3

start_time3 = time.process_time()
array3 = set(shop3)
for i in customer3:
    if i in array3:
        pass
    else:
        pass

end_time3 = time.process_time()
print(f"작동시간3 : {end_time3 - start_time3}")