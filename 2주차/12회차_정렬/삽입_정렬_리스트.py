'''
https://leetcode.com/problems/insertion-sort-list/
Insertion Sort List
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
'''
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_list = ListNode()
        result_head = result_list
        while head:
            while result_list and result_list.next:
                if result_list.val > head.val:
                    break
                result_list = result_list.next

            new_insert = ListNode(result_list.val, None)
            if result_list.next:
                new_insert.next = result_list.next
            result_list.val, result_list.next = head.val, new_insert
            result_list = result_head
            head = head.next
        while result_list and result_list.next:
            if result_list.next.next is None:
                result_list.next = None
            result_list = result_list.next

        return result_head

# 데이터 생성하기
node1 = ListNode(4)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
[0-> 4 ->1 -> 2 ->3 -> None]
# 데이터 연결하기
node1.next = node2
node2.next = node3
node3.next = node4

Solution().insertionSortList(node1)