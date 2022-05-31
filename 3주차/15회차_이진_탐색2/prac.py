# def two_sum(nums, target):
#     left, right = 0, len(nums)-1
#     while left<right:
#     # while left!=right:
#         sum = nums[left]+nums[right]
#         if sum > target:
#             right -=1
#         elif sum < target:
#             left +=1
#         else:
#             return [left,right]
#
# nums = [2,7,11,15]
# print(two_sum(nums, 9))

def check_item(nums, m_list):
    for target in m_list:
        l, r = 0, len(nums) - 1
        while l <= r:
            if target !=nums[l]:
                l += 1
            if target != nums[r]:
                r -= 1
            else:
                print(target)
                print('yes',end=' ')
                break
        if target not in nums:
            print(target)
            print('no', end=' ')

n = [8, 3, 7, 9, 2]
m_list = [5, 7, 9]
check_item(n, m_list)
# for target in m_list:
#     check_item(n, target)