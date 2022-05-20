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
