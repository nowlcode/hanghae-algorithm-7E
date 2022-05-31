'''
나무 자르기
https://www.acmicpc.net/problem/2805

입력:
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다.
(1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에,
상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

출력:
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

4 7
20 15 10 17
'''

n, m = map(int, input().split())
height = list(map(int,input().split()))

start = 0
end = max(height)

while start<=end:
    total = 0
    # 상한 조정하는 값 -> 아님 잘못 이해했음. mid가 아니라 m이 상한값
    mid = (start+end)//2
    for h in height:
        if h > mid:
            total += h - mid
        # else:
        #     end = mid-1
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)