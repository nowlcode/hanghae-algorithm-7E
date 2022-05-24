# 배열 Array 연습
def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(sorted(array[c[0]-1:c[1]])[c[2]-1])
    return answer
# print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


# def solution2(id_list, report, k):
#     answer = []
#     for r in report:
#         a = r.split()
#         return a
#
# print(solution2(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))

def solution3(numbers):
    # numbers 리스트에 있는 숫자들을 하나씩 빼 첫 숫자로 지정한다
    max_list = []
    for i in range(len(numbers)):
        # 첫 숫자 6 그대로. 나머지 숫자만큼 반복
        for j in range(len(numbers)-1):
            answer = ''
            # 첫 숫자로 지정한 다음 그 나머지 (index 0이후의 애들)을 더해준다
            answer += str(numbers[i])
            answer += "".join(map(str,numbers[i+1:len(numbers)]))
            first = numbers.pop(0)
            numbers.append(first)
            # a = numbers[i:len(numbers)]
            max_list.append(answer)

    return max_list
print(solution3([6, 10, 2]))


# 배열 Array 연습


# Linked List 구현

# 스택 구현

# 큐 구현

# 해시테이블 구현