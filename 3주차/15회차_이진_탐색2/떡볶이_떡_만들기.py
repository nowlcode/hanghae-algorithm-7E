n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))
rice_cake.sort()
# [10, 15, 17, 19]

start, end = 1, rice_cake[-1]
'''
19//2
9 자른다
자르고 더한 값 > m:
    좀 덜 잘라야 하니, 자르는 기준 값을 올린다.
자르고 더한 값 < m:
    좀 더 잘라야 하니, 자르는 기준 값을 내린다.
자르고 더한 값 == 같음:
    이거다

target과 일치하는 값이 아닌
target 그 자체를 찾고 있다.

'''


def bs(start, end):
    def cut_rice(x):
        if x > mid:
            return x - mid
        return 0

    if start > end:
        return -1

    mid = (start + end) // 2
    result = sum(map(cut_rice, rice_cake))
    if result < m:
        end = mid - 1
        return bs(start, end)
    elif result > m:
        start = mid + 1
        return bs(start, end)
    else:
        return mid


print(bs(start, end))
'''
7 12
19 15 10 17 16 14 15
'''
# [19, 15, 10, 17]

'''


'''

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에 result 기록
        start = mid + 1

    # 정답 출력
    print(result)
