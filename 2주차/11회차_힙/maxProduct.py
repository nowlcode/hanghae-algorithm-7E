import heapq
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap =[]
        for n in nums:
            # 최소 힙인데 최대힙으로 생성했음
            heapq.heappush(heap,-n)
        # 최대값 2개니까 heappop 2개
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        # 빼고나서 정렬도 시켜줘라 heapq
        # 거기에서 -1을 해줘야한다
        answer = (first-1)*(second-1)
        return answer

s = Solution()
print(s.maxProduct([3,4,5,2]))

# repo: Python print했을 때 실행되는 것
