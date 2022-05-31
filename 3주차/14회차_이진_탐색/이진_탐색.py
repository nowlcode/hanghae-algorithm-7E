'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
회전 정렬된 배열 검색
'''
# 이해를 위한 대충한 로직
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def 재귀(nums,target)
            if start > end
                return -1나가
            중앙 = (start + end)/2

            만약 중앙값이 타겟보다 작으면:
            타겟이 어디있냐 오른쪽에 있겠네
            오른쪽으로 재귀 돌려(중앙값+1, 끝까지)

        만약 중앙값이 타겟보다 크:
            타겟이 어디있냐 왼쪽에 있겠네
            왼쪽으로 재귀 돌려(스타트, 중앙값-1)
        아니면 아 이거네
            타겟 찾았다

        야 타겟찾아봐
        원래 타겟 위치 = 재귀(nums, target)

        if 타겟 위치 = -1:
            return -1

        일단 정렬sort()
        target이 어딨냐
                리턴
        바뀐 타겟 위치값 = 재귀(nums, target)

        # 타겟 위치값 + 몇번 돌렸냐 해야함
        얼마나 돌았냐 = 원래 타겟 위치 - 바뀐 타겟 위치
        return 얼마나 돌았냐 + 바뀐 타겟 위치
'''

def bs_rotated(nums, target):
    def bs(lst, start, end):
        if start > end:
            return -1

        mid = (start + end) // 2
        if lst[mid] < target:
            return bs(lst, mid + 1, end)
        elif lst[mid] > target:
            return bs(lst, start, mid - 1)
        else:
            return mid

    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    added = nums + nums[:left]

    result = bs(added, left, len(added) - 1)
    return result if result == -1 else result % len(nums)
