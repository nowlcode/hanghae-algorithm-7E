from typing import List

# class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for i in matrix:
    #         # [1, 4, 7, 11, 15] 5
    #         if len(i)>0:
    #             if i[0] < target:
    #                 # 0-4
    #                 for _ in range(len(i)):
    #                     left, right = 0, len(i)-1
    #                     mid = (left + right)//2
    #                     print(i[right])
    #                     if i[mid]<target:
    #                         return self.searchMatrix([i[mid+1:right]],target)
    #                     elif i[mid]>target:
    #                         return self.searchMatrix([i[left:mid-1]],target)
    #                     else:
    #                         return True
    #
    #     return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def loop(lst):
            # [1, 4, 7, 11, 15] 5
            if len(lst)>0:
                if lst[0] <= target:
                    # 0-4
                    for _ in range(len(lst)):
                        left, right = 0, len(lst)-1
                        mid = (left + right)//2
                        # print(lst[right])
                        if lst[mid]<target:
                            return loop(lst[mid+1:right+1])
                        elif lst[mid]>target:
                            return loop(lst[left:mid])
                        else:
                            # print('return')
                            return True
        for i in matrix:
            if loop(i):
                return True
        return False


s = Solution()
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],
                      [18,21,23,26,30]],20))

print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        x_start = 0
        x_end = len(matrix[0])-1

        y_start = 0
        y_end = len(matrix)-1

        while 0 <= x_end:
            if x_start > x_end:
                break
            mid = (x_start+x_end)//2
            if matrix[0][mid] < target:
                x_start = mid+1
            elif matrix[0][mid] > target:
                x_end = mid-1
            else:
                return True

        while 0 <= y_end:
            if y_start > y_end:
                break
            mid = (y_start+y_end)//2
            if matrix[mid][0] < target:
                y_start = mid+1
            elif matrix[mid][0] > target:
                y_end = mid-1
            else:
                return True

        for y in range(y_end+1):
            for x in range(x_end+1):
                if matrix[y][x] == target:
                    return True

        return False

