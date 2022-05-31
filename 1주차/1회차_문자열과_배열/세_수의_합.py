def three_sum(nums):
    result = []
    for start in range(len(nums)):
        end = start + 3
        three = nums[start:end]
        if len(nums) > end:
            # if len(three)==3:
            result.append(sum(three))
    print(result)
    return result


nums = [-1, 0, 1, 2, -1, 4]


# print(nums[:3])
# three_sum(nums)