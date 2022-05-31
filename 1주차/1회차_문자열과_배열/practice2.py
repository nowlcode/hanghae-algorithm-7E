# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 첫 부분 .val 숫자를 비교하고 더 크거나 작으면 다음 번 insert
        # 규칙정리: l1 & l2 len 같지만은 않다
        result = []
        while l1 and l2:
            if l1.val < l2.val:
                result.append(l1.val)
                l1 = l1.next
            else:
                result.append(l2.val)
                l2 = l2.next

        while l1:
            result.append(l1.val)
            l1 = l1.next

        while l2:
            result.append(l2.val)
            l2 = l2.next
        head = ListNode()
        head.val = ''
        node = head
        while len(result):
            node.val = result[0]
            if len(result)>1:
                node.next = ListNode()
            node = node.next
            del result[0]

        return head

[1,1,3,4,4,0]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6
s = Solution()
# print(s.mergeTwoLists(node1, node4))

# 첫 부분 .val 숫자를 비교하고 더 크거나 작으면 다음 번 insert
# 규칙정리: l1 & l2 len 같지만은 않다
# self.head = ListNode(l1.val)
# while l1 and l2:
#     if l1.val < l2.val:
#
#         l1 = l1.next
#         while node.next:
#             node = node.next
#         node.next = ListNode(l1.val, None)
#     else:
#         self.head = ListNode(l2.val)
#         node = self.head
#         l2 = l2.next
#         print(node.val)
#         while node.next:
#             node = node.next
#         node.next = ListNode(l2.val, None)
#
# while l1:
#     self.head = ListNode(l1.val)
#     l1 = l1.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution(object):
#
#     def mergeTwoLists(self, l1, l2):
#         result = []
#
#         while l1 and l2:
#             if l1.val < l2.val:
#                 result.append(l1.val)
#                 l1 = l1.next
#             else:
#                 result.append(l2.val)
#                 l2 = l2.next
#         if l1:
#             result.append(l1.val)
#
#         if l2:
#             result.append(l2.val)
#
#         result2 = ListNode()
#         tail = result2
#         for i in range(len(result)):
#             print(i)
#             tail.next = ListNode(result[i])
#             print(result)
#
#     `       tail = tail.next
#
#     return result

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        result = ListNode()
        tail = result
        while l1 and l2:
            print("L1", l1)
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return result.next
# 0-5
# [2,0,2,1,1,0]
# iters = 4
# iter [0-3]
# wall 4 3 2

[1,2,4]
[1,3,4]