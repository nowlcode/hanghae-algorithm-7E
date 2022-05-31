from collections import deque

"""
225. 큐를 이용한 스택 구현

큐를 이용해 다음 연산을 지원하는 스택을 만들어라.

push(x): 요소 x를 스택에 삽입한다
pop(): 첫번째 스택 요소를 삭제
top(): 스택의 첫 요소 가져오기
empty(): 스택이 비어있는지 여부를 리턴
"""

# class MyStack:
#
#     def __init__(self):
#         self.q = deque()
#
#     def push(self, x: int) -> None:
#         self.q.append(x)
#         print(self.q)
#         self.q.reverse()
#         print(self.q)
#
#     def pop(self) -> int:
#         self.q.pop()
#
#     def top(self) -> int:
#         return self.q[-1]
#
#     def empty(self) -> bool:
#         return self.q is True



class MyStack:
    def __init__(self):
        # Queue클래스 소유의 q변수를 만들고 deque를 안에 넣어준다
        self.q = deque()

    def push(self,x):
        self.q.append(x)
        # print(self.q)
        for _ in range(len(self.q)-1):
            # print(self.q, 'HI')
            self.q.append(self.q.popleft())
            # print(self.q)

    def pop(self):
        # while not self.q:
        #     return None
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q)==0


c = MyStack()
c.push(1)
c.push(2)
c.push(3)
top = c.top()
pop = c.pop()
emp = c.empty()

"""
232. 스택을 이용한 큐 구현

스택을 이용해 다음 연산을 지원하는 큐를 구현하라.

push(x): 요소 x를 스택의 마지막에 삽입한다
pop(): 큐 처음에 있는 요소를 삭제
top(): 큐 첫 요소 조회하기
empty(): 큐가 비어있는지 여부를 리턴
"""

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self,x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
            return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


cue = MyQueue()
cue.push(1)
cue.push(2)
# peek함수를 pop함수보다 먼저 불러오니 pop에서 peek를 사용한 것에 대한 에러가 안 뜸.
cue.peek()
cue.pop()
cue.empty()

