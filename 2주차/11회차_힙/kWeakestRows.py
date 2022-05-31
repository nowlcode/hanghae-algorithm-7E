from collections import Counter as ct
from typing import List
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        """
        heap = []
        for i in range(len(mat)):
            t1 = ct(mat[i])
            heapq.heappush(heap, t1[1] + i * (10 **(-2) ) )
        answer = []
        for i in range(k):
            t3 = heapq.heappop(heap)    # t3 = 1.001
            t2 =  str(t3).split(".")[1][:2]
            while len(t2) < 2:
                t2 += '0'
            answer.append( int(t2) )
        return answer


s = Solution()
s.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3)


from collections import Counter as ct
from typing import List
import heapq

class Solution2:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            heapq.heappush(heap)
        return heap