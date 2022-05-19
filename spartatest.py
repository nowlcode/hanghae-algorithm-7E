'''
전화번호 목록
Description
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

입출력 예제
phone_book	                            return
["119", "97674223", "1195524421"]	    false
["123","456","789"]	                    true
["12","123","1235","567","88"]	        false
'''

def solution(phone_book):
    # 제일 작은 첫번째의 길이를 구해 다른 번째 애들 prefix길이가 어떤지 찾음 -> prefix other_num비교
    # 찾아서 그 첫 부분만 비교함
    # 첫번째 애보다 길이가 작으면 막바로 트루 -> No, 다른 애들도 생각해야지 -> 필요없을듯
    # print(phone_book)
    phone_book = sorted(phone_book)
    # 프리픽스부터 바꿔줘야함!!
    prefix = phone_book[0]
    prefix_len = len(phone_book[0])
    # 폰북에 있는 모든 번호 돌림
    for i in range(len(phone_book)):
        # 만약 접두사가 번호의 앞과 같다면
        if prefix==phone_book[i][:prefix_len] and i!=0:
            check = 0
            return check>0
        elif i==0:
            pass
        else:
            check=1
    # print(check)
    return check==1


# from itertools import combinations as c
# def solution(phoneBook):
#     answer = True
#     sortedPB = sorted(phoneBook, key=len)
#     print(sortedPB)
#     for (a, b) in c(sortedPB, 2):
#         print(c(sortedPB,2))
#         if a == b[:len(a)]:
#             answer = False
#     return answer


def solution(phone_book):
    phone_book = sorted(phone_book)
    print(phone_book)
    prefix = phone_book[0]
    prefix_len = len(phone_book[0])
    # print(phone_book, prefix)
    for i in range(len(phone_book)):
        if prefix==phone_book[i][:prefix_len] and i!=0:
            check = 0
            return check>0
        elif i==0:
            pass
        else:
            check=1
    return check==1

    # if phone_book[0] in phone_book[2]:
    #     print('Yep')
    # else:
    #     print('Not here')

# # solution(["119", "97674223", "1195524421"])
# print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123","456","789"]))
# print(solution(["12","123","1235","567","88"]))
# print(solution(["12","1","1","5","88"]))
# print(solution(["97674223", "119", "1195524421"]))



'''
기능개발
Description
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가
주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

입출력 예
progresses	                        speeds	return
[93, 30, 55]	                    [1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
'''
# import math
# def solution2(progresses, speeds):
#     answer = []
#     blank = {}
#     #100먼저 완성시키려면 걸리는 기간 구하기 (3.4나오면 4로 올려주기)
#     for i in range(len(progresses)):
#         days_to_complete =  math.ceil((100-progresses[i])/speeds[i])
#         # 끝내는 기간이 blank에 없으면 추가
#         if days_to_complete not in blank:
#             blank[days_to_complete]=1
#         # 끝내는 기간이 blank에 있으면 하나 더 추가
#         else:
#             blank[days_to_complete]+=1
#     # 그럼 blank에는 {프로젝트 걸리는 기간: 프로젝트 개수}이렇게 될 것임.
#     # 여기서 key를 넣어보자
#     days = list(blank.keys())
#     sum1 = 0
#     for j,a in enumerate(days):
#         # 첫기능 기간이 a의 기간보다 길 때 더해준다
#         if days[0]>=a:
#             sum1 += blank[a]
#         else:
#             answer.append(blank[a])
#     answer.insert(0,sum1)
#
#     return answer

#뭘 잘 못 생각했는지 알겠다. 난 전체를 봤고, 문제는 queue로 바로 다음 애가 기간이 작지 않으면 리턴 안 하네.



# import math
# import collections
# def solution2(progresses, speeds):
#     answer = []
#     blank = {}
#     #100먼저 완성시키려면 걸리는 기간 구하기 (3.4나오면 4로 올려주기)
#     for i in range(len(progresses)):
#         days_to_complete =  math.ceil((100-progresses[i])/speeds[i])
#         # 끝내는 기간이 blank에 없으면 추가
#         if days_to_complete not in blank:
#             blank[days_to_complete]=1
#         # 끝내는 기간이 blank에 있으면 하나 더 추가
#         else:
#             blank[days_to_complete]+=1
#     # 그럼 blank에는 {프로젝트 걸리는 기간: 프로젝트 개수}이렇게 될 것임.
#     # 여기서 key를 넣어보자
#     days = collections.deque()
#     for k, v in blank.items():
#         days.extend([k]*v)
#
#     print(days)
#     # 첫번째가 두번째보다 작으면 answer에 하나 append
#     count = 0
#     #투포인터 - queue를 써서 맨 앞에 있는 애랑 다음 애랑 비교. 다 했으면 앞의 애들만 pop/remove
#     left = 0
#     right = left+1
#     while days:
#         # 데크에 하나 밖에 안 남았으면 append해주고 pop해서 지워주면 됨.
#         if len(days)==1:
#             print(len(days), 'length1')
#             print(days,'isit')
#             count = 0
#             answer.append(1)
#             days.popleft()
#             print(answer, 'one')
#         # 현재번째 기간이 다음번째 기간보다 작을 때 하나 추가하고 pop해서 지워줌.
#         elif days[left] < days[right] and len(days)>1:
#             print(len(days),'lengthsmall')
#             answer.append(1)
#             days.popleft()
#             print(answer,'small')
#             print(days, 'what')
#         # 현재번째 기간이 다음번째 기간보다 크거나 같을 때 (left이용함) 하나씩 count에 추가
#         elif days[left] >= days[right]:
#             print(len(days),'lengthbig')
#             count += 1
#             days.popleft()
#             if days[left]<days[right]:
#                 # print(count, 'o')
#                 answer.append(count)
#                 print(answer, 'big-o')
#                 print(len(days), 'lengthbig')
#                 days.popleft()
#                 count = 0
#
#
#             print(answer, 'big')
#
#     return answer

import math
import collections
def solution2(progresses, speeds):
    answer = []
    stack = []
    #100먼저 완성시키려면 걸리는 기간 구하기
    for i in range(len(progresses)):
        # (3.4나오면 4로 올려주기)
        days_to_complete = math.ceil((100-progresses[i])/speeds[i])
        # progresses 순서대로 걸린 기간 넣기
        stack.append(days_to_complete)
    # 데크를 만들어줌
    days = collections.deque(stack)
    print(days)
    count = 0
    #투포인터 - queue를 써서 맨 앞에 있는 애랑 다음 애랑 비교. 다 했으면 앞의 애들만 pop/remove
    # left = 0
    # right = left+1
    # days에 아직 아이템이 있을 때 계속 루프
    while days:
        # print(days)
        if len(days)==1:

            answer.append(count+1)
            days.popleft()
            # print(days)
            # print(answer)
        elif days[0]<days[1]:
            answer.append(count+1)
            days.popleft()
            count = 0
            # print(answer)
        else:
            count+=1
            days.popleft()
            # print(answer)
    return answer

# print(solution2([93, 30, 55],[1, 30, 5]))
# print(solution2([95, 90, 99, 99, 80, 1], [1, 1, 1, 1, 1, 1]))
# print(solution2([95,90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# print(solution2([90,90,40, 99, 80, 99], [1, 1, 1, 1, 4, 1]))
# print(solution2([99, 80, 99], [1,1,1]))

# [5]<s [10b,1b,1]<s [20b,1]<o
