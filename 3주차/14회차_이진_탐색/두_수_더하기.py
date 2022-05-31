'''
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''


class Solution:
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        already = set()
        for idx, number in enumerate(numbers):
            value = target - number
            if value not in already:
                if value in numbers[idx+1:]:
                    return [idx+1,numbers[idx+1:].index(value)+idx+2]
            already.add(number)

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            cal_sum = numbers[left] + numbers[right]
            if cal_sum > target:
                right -= 1
            elif cal_sum < target:
                left += 1
            else:
                return left + 1, right + 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, cur_num in enumerate(numbers):
            expected = target - cur_num
            left, right = idx + 1, len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return idx + 1, mid + 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, cur_num in enumerate(numbers):
            expected = target - cur_num
            import bisect
            i = bisect.bisect_left(numbers, expected, idx + 1)     # 현재 cur_num의 [idx+1~끝] 범위에 target이 있는지 검사
            if i < len(numbers) and numbers[i] == expected:    # 만약 target이 존재하면
                return idx + 1, i + 1
