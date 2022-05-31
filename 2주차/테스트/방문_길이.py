from collections import Counter

def solution(dirs):
    """
    1) 반복 x 원점으로 온 visited
    2) 평면 경계 넘으면 x
    """
    answer = 0
    # 방법1: dfs때랑 비슷하게 이미 방문 한 곳을 visited로 만들어 반복 안 하게 함.

    # if d == 'U':
    #     x += 1
    # elif d == 'D':
    #     x -= 1
    # elif d == 'R':
    #     y += 1
    # elif d == 'L':  # or do else instead
    #     y -= 1

    # 시작점은 (x0,y0)
    x,y = 0,0
    visited = [(x,y)]
    # print(list(dirs))
    # 각 명령어를 읽는다
    for d in dirs:
    # 좌표를 구함. U: (x+1,0), D: (x-1,0), L: (x0,y-1), R: (x0,y+1)


    print(visited)
    answer = len(visited)-1
    return answer

# print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))
print(solution("LLLLLRRRRRRUUUUUDDDDDD"))
print(solution("RRRRRRR"))


# (x,y) not in visited and (x<5 or x>-5 and y<5 or y>-5)

# 방법2: 반복되기 전 원점 찾음.
# 반대 팰린드롬 체크. 예) 'LL|RR', 'LUR|RDL' 근데 이렇게 일일히 체크하게 만드는 과정이 복잡할 것 같다.

# 평명 경계 넘지 않게 해야함.
# # 방법1: 각 U,D,L,R을 count한다. {'U':3,'D':2...} 이런 식으로 될 거다.
# count = Counter(dirs)
# # U의 갯수와 D의 갯수의 차이, 또는 L의 갯수와 R의 갯수의 차이가 5이상 나면 무시한다
# if abs(count['U']-count['D'])>5 or abs(count['L']-count['R'])>5:
#     pass

# #방법2: x,y가 -5랑 5사이가 되면 됨.
# if x>5 or x<-5 or y>5 or y<-5:
#     pass