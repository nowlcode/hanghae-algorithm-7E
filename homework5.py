import collections
'''
706. 해시맨 디자인
다음의 기능을 제공하는 해시맵을 디자인하라
put(key, value): 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.
get(key):키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1을 리턴한다.
remove(key): 키에 해당하는 키, 값을 해시맵에서 삭제한다.
'''

class MyHashMap:
    def __init__(self):
        self.map = {}

    def put(self, key, value):
        if key not in self.map:
            # self.map[key] = value
            self.map.update({key: value})
        else:
            # self.map.update({key: value})
            # 위는 그냥 append 되는 식이다. 이미 존재하는 딕셔너리에 key, value가 삽입된다.
            self.map[key] = value # 해당 키의 해시값이 바뀐다

    def get(self, key):
        if key not in self.map:
            return -1
        return self.map.get(key) #or try self.map[key]

    def remove(self,key):
        if key in self.map:
            self.map.pop(key)


hashMap = MyHashMap()
hashMap.put(1,1)
hashMap.put(2,2)
hashMap.get(1)          # return 1
hashMap.get(3)          # return -1 (key doesn't exist)
hashMap.put(2,1)        # update hash value
hashMap.get(2)          # return 1
hashMap.remove(2)       # delete key, value for key 2
hashMap.get(2)          # return -1 (key deleted and doesn't exist)

class ListNode:
    def __init__(self,key=None,value=None):
        # key, value, next를 하나의 ListNode로 묶어주기
        # 처음에는 key, value 없음 None
        self.key = key
        self.value = value
        self.next = None

class MyHashMap2:
    # 초기화
    def __init__(self):
        # 공간이 1000인 해시테이블 만들기
        self.size = 1000
        self.table = collections.defaultdict(ListNode) #defaultdict사용해 키 안 만들어줘도 티폴트 줘서 에러 안 남.

    #삽입
    def put(self, key: int, value: int) -> None:
        # 1000번째 인덱스는 0이다. 그 전까지는 mod이용 1-999나머지가 그대로 나온다
        # 한 마디로 key==index if index<=1000
        index = key%self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key,value)
            # 업데이트는 어딨지?? ListNode next로 다음을 가르켜 이미 해주는 건가???
            return
        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key,value)

    #조회
    def get(self, key: int) -> int:
        index = key%self.size
        # self.table[index]가 노드라서 .value해줘야 함. 아닌가? 노드들이 들어갈 수 있는 공간이라해야 하나?
        # linked list 체이닝 방식이니 첫 노드라고 보는게 맞겠다.
        if self.table[index].value is None:
            return -1

        # 노드 존재할 때 일치하는 키 탐색
        p = self.table[index]
        # p는 전체 테이블이니 막바로 if p.key == key할 수 없음. 그래서 while으로 돌려줘야함.
        while p:
            if p.key == key:
                return p.value
            p = p.next
        # ??? 왜 다시 해주지?
        # 혹시 첫 노드에서 None이 안 나왔더라도 나중에 그 인덱스 안에 들어올 다른 노드들의 value가 없으면 -1해주는 걸까?
        return -1

    #삭제
    def remove(self, key: int) -> None:
        index = key%self.size
        if self.table[index].value is None:
            return
        # 인덱스 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        # 첫 노드니까 while 안 쓰고 키 맞으면 삭제 처리됨.
        if p.key==key:
            # p.value = p.next
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트에 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next




'''
771. 보석과 돌
J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.

예시:
Input: J = "aA, S = "aAAbbbb"
Output: 3

문제 표현 때문에 헷갈렸다. 문제의 output이 3이라 왜 그런지 계속 고민하다가 다른 풀이들 읽어보며 이해했다.
https://deep-learning-study.tistory.com/356 리스트 컴프리헨션 부분
한 마디로 J안에 속해있으면 보석이다. 'aA'에서 'a'나 'A'만 있어도 보석 취급한다는 소리. 
그래서 S는 'aAA' 3개가 J에 속함으로 output이 3이다.
'''

class Jewels:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 해시 테이블 개설: stones의 각 letter가 key, value는 count된 숫자
        # {'a':1, 'A':2,'b':4}
        stone_count = collections.Counter(stones)
        # sum은 각 jewels letter가 count된 숫자를 더해주는 것
        sum = 0
        # 각 jewels letter가 stone_count 콜렉션에 있는지 확인해주고,
        # 있으면 sum에 해당 letter count 숫자를 더해준다
        for j in jewels:
            if j in stone_count:
                sum+=stone_count[j]
        return sum

class Jewels2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for j in jewels:
            if j in stones:
                counter += stones.count(j)
        return counter


'''
3. 중복 문자 없는 가장 긴 부분 문자열
중복 문자가 없는 가장 큰 부분 문자열 substring을 리턴하라

input: 'abcabcabc'
output: 'abc'

input: 'bbbbb'
output: 'b'
'''
# class SubString:
#     def lengthOfLongestSubstring(self, string: str) -> int:
#         # 해시 문제니까 딕셔너리 만들어서 할까? 근데 딕셔너리로 생각하려니 복잡해질 것 같다.
#         # empty []를 만들어 for loop돌려서 s내에 반복하지 않는 letter들을 각자 더해준다.
#         # 아님 슬라이싱을 해볼까?? 반복 안 될 때
#         # 반복되는 letter가 나오면 for loop break 시키고 empty에 남은 애들을 "".join()해서 리턴한다.
#         empty = []
#         for s in string:
#             # 문제! 이러면 반복 안 되는 부분들 빼고 전체가 온다구..
#             if s in empty:
#                 # 여기서 break하면 if문만 나가게 될까 아님 for문도 나가는 걸까?
#                 break

class SubString:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        #이렇게 할 수도 있구나.. 일단 max_length와 start 둘 다 0부터 시작
        max_length = start = 0
        # 각 index와 s글자를 돌림.
        for index, char in enumerate(s):
            #여기서부터 무슨 말인지 모르겠다.
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                # 왜? 알 것 같으면서도... index+1-start는 현재 보는 글자 string max 숫자
                max_length = max(max_length,index-start+1)

            used[char] = index
        return max_length


'''
최댓값과 최솟값

Description
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
입출력 예
    s           return
"1 2 3 4"	    "1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	        "-1 -1"
'''

def solution(s):
    answer = ''
    return answer

'''
주식가격
Description
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	        return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
'''

def solution(prices):
    answer = []
    return answer


'''
프린터
Description
일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

제한사항
현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.
입출력 예
priorities	        location	return
[2, 1, 3, 2]	        2	        1
[1, 1, 9, 1, 1, 1]	    0	        5
입출력 예 설명
예제 #1

문제에 나온 예와 같습니다.

예제 #2

6개의 문서(A, B, C, D, E, F)가 인쇄 대기목록에 있고 중요도가 1 1 9 1 1 1 이므로 C D E F A B 순으로 인쇄합니다.
'''


def solution(priorities, location):
    answer = 0
    return answer


'''
A Correct Parenthesis
Description
The definition of correctly paired parentheses means that if it is opened with a '(' character, it must be closed with a ')' character.
For instance,

"()()" or "(())()" is a correct parenthesis.
")()(" or "(()(" is an incorrect parenthesis.
Given a string s consisting only of '(' or ')', complete a solution function that returns true if the string s is the correct parenthesis and false if it is not.

Constraints
Length of string s: natural number less than 100,000
The string s consists of only '(' or ')'.
Example
s	        answer
"()()"	    true
"(())()"	true
")()("	    false
"(()("	    false
Example #1

Same as above example.
'''

def solution(s):
    answer = True

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True