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


### GROUP ANAGRAM ###
l2 = []


# l2 = {}
def anagram(str_list):
    l = {}
    for i in range(len(str_list)):
        word = "".join(sorted(str_list[i]))
        if word not in l:
            l[word] = [str_list[i]]
        else:
            l[word] += [str_list[i]]
    return l.values()


l1 = ["eat", "tea", "tan", "ate", "nat", "bat"]


# print(anagram(l1))

### LONGEST PALINDROME SUBSTRING ###
def longpalindrome(s):
    # 팰린드롬 판별
    if s == s[::-1]:
        return s
    else:
        sub = []
        for n1 in range(len(s)):
            for n2 in range(n1 + 1, len(s)):
                substring = s[n1:n2 + 1]
                print(n1, n2, substring)
                # print(s[n1]==s[n2],palindrome(substring))
                if (s[n1] == s[n2] and palindrome(substring)):
                    sub.append(substring)
                else:
                    sub.append(substring[0])
        return max(sub, key=len)


# longpalindrome('babad')
# a = 'apple'
# print(a[1:-1])

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def palindrome(s: str) -> str:
#             #소문자에 알파벳과 숫자만 표시하기
#             string = list("".join(s.lower().split()))
#             for i in range(len(string)):
#                 if not string[i].isalnum():
#                     string[i] = " "
#             string = "".join("".join(string).split())
#
#             #반 쪼개서 중간서부터 비교하기
#             length = int(len(string)/2)
#             if len(string)%2==0:
#                 return string[:length]==string[:length-1:-1]
#             else:
#                 return string[:length]==string[:length:-1]
#
#         if s==s[::-1]:
#             return s
#         else:
#             sub = []
#             for n1 in range(len(s)):
#                 next = s[n1+1:]
#                 for n2 in range(len(next)):
#                     n2=n1+n2+1
#                     substring = s[n1:n2+1]
#                     if (s[n1]==s[n2] and palindrome(substring)):
#                         sub.append(substring)
#                     else:
#                         sub.append(substring[0])
#             return max(sub, key=len)

def three_sum(nums):
    result = []
    for start in range(len(nums)):
        end = start + 3
        three = nums[start:end]
        if len(nums) > end:
            # if len(three)==3:
            result.append(sum(three))
    print(result)
    return result


nums = [-1, 0, 1, 2, -1, 4]


# print(nums[:3])
# three_sum(nums)


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