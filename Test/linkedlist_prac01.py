#테스트 케이스 개수
T = int(input())
#결과값 표시
result = []

#dfs 메서드 함수
def dfs(num,sum):
    global count
    # 더한 값이 구하는 값보다 크다면 return
    if num<sum:
        return
    # 더한 값이 구한 값과 같다면 개수 추가
    if num==sum:
        count+=1
        return
    for i in range(1,4):
        sum+=1
        #dfs 재귀적 수행
        dfs(num,sum)
        sum-=1

# 입력받고 dfs 메서드 수행
for _ in range(T):
    num = int(input())
    count=0
    dfs(num,0)
    result.append(count)

# 결과 출력
for answer in result:
    print(answer)