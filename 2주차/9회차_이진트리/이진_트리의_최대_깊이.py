import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self,root) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        print(depth)
        return depth


# root = [3, 9, 20, None, None, 15, 7]
# s = Solution()
# print(s.maxDepth(root))


# def multiply(n1,n2):
#     m=n1*n2
#     return m
# print(multiply(3,4))
# root= TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left=TreeNode(15)
# root.right.right = TreeNode(7)
# assert s.maxDepth(root)==3

import collections


def make_tree_by(lst, idx):
    parent = None
    # print("길이:",len(lst),"|인덱스:",idx)
    if idx < len(lst):
        value = lst[idx]
        # print("노드의 값",value)
        if value == None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth


root1 = [3, 9, 20, None, None, 15, 7]
root = make_tree_by(root1, 0)
s = Solution()
print(s.maxDepth(root))