class Node:
    def __init__(self,value,next):
        self.value = value # attribute 지정, attribute name not built-in or fixed as I can create the name
        self.next = next

class Stack:
    def __init__(self):
        #stack안에 class property==attribute 소유물인 self.top을 만들어줌.
        self.top = None

    def push(self, val):
        self.lst = []
        for v in val:
            # self.top을 빈 리스트/컨테이너 공간이라고 생각했는데 노드 안에 그걸 넣어버리니까, 그럼 next로 포인트되는 self.top을 그리지 못하겠음.
            # 살짝 이해 안  -> 그림 그리니 이해감. var과 value를 혼동함.
            # self.top value인 None을 next에 넣어두고 self.top은 이제 노드가 됨.
            self.top = Node(v,self.top)
            # print(self.top.value)
            self.lst.append(self.top.value)
        # print(self.lst)
        return self.lst

    def pop(self):
        # self.top에 아무것도 없으면 그대로 return None해준다.
        #스택에 아무것도 없어서 안 받아가는 것과 같다. 뭔가 아마존 메일박스에 패키지 넣으면 뒤쪽에서 auto 쓸어담는 것과 비슷.
        while not self.top:
            return None
        # 스택에 물건이 있다하면, 위에 있는 노드 value를 node var에 담아두고,
        node = self.top
        # print(node.value)
        # self.top attr var에는 self.top.next value를 담아둔다.
        self.top = self.top.next
        return node.value

    def is_empty(self):
        # self.top에 아무것도 없는게 맞으면 True, 있으면 False리턴해라.
        return self.top is None

    def all_stack(self):
        return self.lst


mstack = Stack()
mstack.push([1,2,3,5,4])
# mstack.push(2)
# mstack.push(3)
# mstack.push(5)
# mstack.push(4)
print(mstack.pop())
print(mstack.pop())
# mstack.push(4)
print(mstack.is_empty())
print(mstack.all_stack())