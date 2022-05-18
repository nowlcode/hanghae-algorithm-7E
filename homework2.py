# 2회차 : 8장 연결 리스트
class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self, to):
        print(f"hello {to}, I'm {self.name}")


rtan = Person("rtanny")
rtan.sayhello("hanghae")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        # print(node.val)
        while node.next:
            node = node.next
            # print(node.val)
        node.next = ListNode(val, None)

lst = [1,2,3]
l1 = LinkedList()
for e in lst:
    l1.append(e)
# print(l1.head.val)

class ReverseList:
    def reverseList(self,head:ListNode) -> ListNode:
        def reverse(node:ListNode,prev:ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)

# r = ReverseList()
# print(r.reverseList([1,2,3,4,5]))

# result = result[0] if result else None
    def print_nodes(self):
        if not self.head:
            return False
        node=self.fhead
        while node:
            print(node.val, end=' ')
            node=node.next
        print()
        return True
    listNode = ListNode()






## 역순 연결 리스트 ##

## 두 정렬 리스트의 병합 ##


## 홀짝 연결 리스트 ##

