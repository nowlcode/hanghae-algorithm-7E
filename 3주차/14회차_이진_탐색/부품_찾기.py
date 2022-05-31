'''
동빈이네 전자 매장에는 부품이 N개 있음
각 부품은 정수 형태의 고유 번호가 있음
손님이 M개 종류의 부품을 대량 구매한다고 견적 요청
동빈이는 M개 종류 모두 확인해야함
가게 안에 부품이 모두 있는지 확인하는 프로그램

n = 5
[8, 3, 7, 9, 2]

5
8 3 7 9 2

손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 Yes 없으면 No
구분은 공백으로

입력조건
 - 첫재 줄에 정수 N이 주어진다.( 1 <= N <= 1,000,000)
 - 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어딘다. 이떄 정수는 1보다 크고, 1,000,000 이하이다.
 - 셋째 줄에는 정수 M 주어진다.
 - 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이떄 정수는 1보다 크고, 1,000,000 이하이다.

출력 조건
 - 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 No


5
8 3 7 9 2
4
3 2 4 5

yes yes no no
'''
def binary_search(nums, target):
    def bs(start, end):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] < target:
            return bs(mid + 1, end)
        elif nums[mid] > target:
            return bs(start, mid - 1)
        else:
            return mid

    return bs(0, len(nums) - 1)

# n = int(input())
# shop = list(map(int, input().split()))
# shop.sort()
# m = int(input())
# customer = list(map(int, input().split()))
#
# for idx in range(m):
#     target = customer[idx]
#     result = binary_search(shop, target)
#     if result != -1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
#
# end_time = time.process_time()










'''
입력조건: 
1. 첫 줄 정수 N 주어짐
2. 공백으로 구분해서 N개의 정수가 주어짐


'''





#
# def binary_search(nums, ):
#     # n = int(input())
#     # arr1 = input()
#     # m =
#     # arr2 =

a = [1,2,3,4]
# print(a[:2])
# mid-1
# [low, mid]
# (start, mid-1)


n = 5
n_list = [8, 3, 7, 9, 2]
m = 3
m_list = [5,7,9]
n_list.sort()
#2 3 7 8 9

def search(n_list, target):
    low, high = 0, len(n_list)-1
    #mid == 2
    mid = (high + low) // 2
    if len(n_list) > 0:
        if target == n_list[mid]:
            print('yes', end=' ')
        elif target > n_list[mid]:
            return search(n_list[mid + 1 : high+1], target)
        elif target < n_list[mid]:
            return search(n_list[low : mid], target)
    if target not in n_list:
        print("no", end=' ')

for target in m_list:
    search(n_list, target)


def check_item(nums, m_list):
    l, r = 0, len(nums)-1
    for m in m_list:
        while l<=r:
            if m==nums[l] or m==nums[r]:
                print('yes', end=' ')
            elif m!=nums[r]:
                r-=1
            else:
                l+=1
        print('no', end=' ')





n = [8,3,7,9,2]
m = [5,7,9]
check_item(n,m)