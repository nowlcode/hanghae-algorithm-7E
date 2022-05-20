### PALINDROME ###
text = 'A man, a plan, a canal: Panama'
text2 = 'race a car'


def palindrome(string):
    # 소문자에 알파벳과 숫자만 표시하기
    string = list("".join(string.lower().split()))
    for i in range(len(string)):
        if not string[i].isalnum():
            string[i] = " "
    string = "".join("".join(string).split())

    # 반 쪼개서 중간서부터 비교하기
    length = int(len(string) / 2)
    if len(string) % 2 == 0:
        return string[:length] == string[:length - 1:-1]
    else:
        return string[:length] == string[:length:-1]


# print(palindrome(text))
# palindrome(text)

def isPalindrome(x: int) -> bool:
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    left, right = 0, len(x) - 1
    while left >= 0 and right < len(x) and left <= right:
        left += 1
        right -= 1
        if x[left] == x[right]:
            return False
    return True

# p = Palindrome()
# print(isPalindrome(1234321))



'''
class Solution(object):
    def mergeTwoLists(self, list1, list2):
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Merge():
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 정렬하기 위한 배열
        list = []


        # 데이터 배열에 담기
        while l1: # l1이 존재할때
            print(l1.val)
            list.append(l1.val)
            l1 = l1.next
            print(l1)
        while l2:
            print(l2.val)
            list.append(l2.val)
            l2 = l2.next
            print(list)

        temp = None
        head = None  # 새로 만든 리스트

        for val in sorted(list):
            # print(val,sorted(list),sep='과')
            # temp 없을 때(빈 리스트), 새로운 node를 생성하고 result에 담는다.
            if not temp:
                temp = ListNode(val)
                print(temp.val)
                head = temp
                # print(head.val)
            # temp 있을 때, 현재 node의 다음 node에 새로운 node를 생성하고
            # 현재 node와 연결해준다.
            else:
                temp.next = ListNode(val)
                temp = temp.next
                print(head.val,temp.val)

        return head


m = Merge()
print(next(m.mergeTwoLists(ListNode([1,2,4]), ListNode([1,3,4])).next))


#