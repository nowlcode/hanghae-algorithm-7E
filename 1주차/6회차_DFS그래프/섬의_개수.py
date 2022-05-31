'''

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
'''
# graph = {
#         1:[2,3,4],
#         2:[5],
#         3:[5],
#         4:[],
#         5:[6,7],
#         6:[],
#         7:[3]
# }

# def recursive_dfs(v,discovered=[]):
#     discovered.append(v)





class Solution:
    def numIslands(self, grid):
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return
            grid[i][j] = '0'
            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        #어떻게 접근할까? [0-3][0-4]있는데 [0][0]애는 [0][1]과 [1][0]과 인접하다.
        #DFS형식으로 밑으로 체크하자
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(i,j)
                    count+=1
        return count

s = Solution()
print(s.numIslands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        height = len(grid)
        width = len(grid[0])
        res = 0

        def dfs(i, j):
            if i < 0 or i >= height or j < 0 or j >= width:
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for dic in direc:
                dfs(dic[0] + i, dic[1] + j)

        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return 0

            grid[r][c] = '0'

            for i, j in zip((r - 1, r + 1, r, r), (c, c, c - 1, c + 1)):
                dfs(i, j)

            return 1

        return sum(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        sum = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "0":
                    continue
                else:

                    # sum up only once per chance of meeting "1"
                    sum += 1
                    stack = list()
                    stack.append([i, j])

                    # visit each "1" in the adjacent area using a stack
                    while len(stack) != 0:

                        [p, q] = stack.pop()

                        if p >= 1 and grid[p - 1][q] == "1":
                            stack.append([p - 1, q])

                        if p < m - 1 and grid[p + 1][q] == "1":
                            stack.append([p + 1, q])

                        if q >= 1 and grid[p][q - 1] == "1":
                            stack.append([p, q - 1])

                        if q < n - 1 and grid[p][q + 1] == "1":
                            stack.append([p, q + 1])

                        # mark as visited
                        grid[p][q] = "0"

        return sum