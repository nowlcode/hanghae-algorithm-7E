
class Solution(object):
    def twoSum(self, nums, target):
        result = []
        # list(map(lambda i: list(map(lambda j: result.append([i, j]) if target == nums[i]+nums[j])), nums))
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if target == nums[i]+nums[j]:
        #             result+=[i,j]
        return result
t = Solution()
# t.twoSum([2,7,11,15],9)

# X = [0, 1, 2]
# Y = [100, 200, 300]
# n = []
#
# n [100,200,300,101,201,301,102,202,302]



# LinkedList와 ListNode공부
class Node:
    #Node는 divided into value and pointer
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next

        return node.item

    def is_empty(self):
        return self.top is None

'''s = Solution()
print(s.removeDuplicate('bcabc'))'''


def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    dict = {}
    list = []
    for i, a in enumerate(alphabet):
        dict[a] = i + 1

    for t in text:
        t = t.lower()
        if t not in alphabet:
            pass
        else:
            print(t)
            list.append(str(dict[t]))
    return " ".join(list)

print(alphabet_position("The sunset sets at twelve o' clock."))
