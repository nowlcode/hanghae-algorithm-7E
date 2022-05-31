'''
예산
https://www.acmicpc.net/problem/2512

입력:
첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다.
다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다.
이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다.
M은 N 이상 1,000,000,000 이하이다.

출력:
첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다.

예:
전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자.
이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고
그 합이 484로 가능한 최대가 된다.

4
120 110 140 150
485

'''

# 상한액 = mid, 합 = 최대길이
n = int(input())
lst = list(map(int, input().split()))
bud = int(input())
# def budget(lst, bud):
#     start = 0
#     end = lst[-1]
#
#     while (start<=end):
#         # 조정해서 상한값 구하기
#         total = 0
#         mid = (start+end)//2
#         for x in lst:
#             # 잘랐을 때의 떡의 양 계산
#             if x > mid:
#                 total += x - mid
#         # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
#         if total < bud:
#             end = mid - 1
#         # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
#         else:
#             result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에 result 기록
#             start = mid + 1
#     print(total)

def budget(lst, bud):
    start = 0
    end = lst[-1]

    while (start<=end):
        total = 0
        mid = (start+end)//2
        for x in lst:
            if x < mid:
                total += x
            else:
                total += mid
        #예산과 합 비교
        if total > bud:
            end = mid-1
        else:
            result = mid
            start = mid+1
    print(result)

budget(lst, bud)

n = int(input())
lst = list(map(int, input().split()))
bud = int(input())

start = 0
end = max(lst) #lst[-1]
# 무제한일때
if sum(lst) <= bud:
    # 들어온 리스트의 최대값을 상한값으로 지정해준다
    print(max(lst))

else:
    while (start <= end):
        total = 0
        mid = (start + end) // 2
        for x in lst:
            if x < mid:
                total += x
            else:
                total += mid
        # 예산과 합 비교
        if total > bud:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)