from collections import Counter
'''
중복된 문자를 제외하고 사전식 순서(lexicographical order)로 나열하라
'bcabc' -> 'abc'
'cbacdcbc' -> 'acdb'
'''

## 중복 문자 제거 ##
class Solution():
    def removeDuplicate(self, strs:str):
        result = []
        # 중복부터 없애기
        counter = Counter(strs)
        print(counter)
        for c in counter:
            result.append(c)
        print(result)



r = Solution()
r.removeDuplicate('bcabc')
# r.removeDuplicate('cbacdcbc')

class Solution:
    def removeDuplicate(self,s:str)->str:
        lookup = {}
        for i in range(len(s)):
            lookup[s[i]]=i
        stack = []
        seen = set()
        for i in range(len(s)):
            if s[i] in seen: continue
            while stack and stack[-1]>s[i] and lookup[stack[-1]]>i:
                seen.remove(stack[-1])
                stack.pop()
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)