
# a: str = 1
# print(a)
# print(type(a))

# def fn(a:int) -> bool:

text = 'A man, a plan, a canal: Panama'
text2 = 'race a car'

## 팰린드롬 ##
def palindrome(string):
    #소문자에 알파벳과 숫자만 표시하기
    string = list("".join(string.lower().split()))
    for i in range(len(string)):
        if not string[i].isalnum():
            string[i] = " "
    string = "".join("".join(string).split())

    #반 쪼개서 중간서부터 비교하기
    length = int(len(string)/2)
    if len(string)%2==0:
        return string[:length]==string[:length-1:-1]
    else:
        return string[:length]==string[:length:-1]
# print(palindrome(text))
# palindrome('applelppa')



# a = 'orange'
# length = int(len(a)/2)
# # print(text[10])
#
# b = a[:3:-1]
# print(b)

## K번째 수 ##
def solution(array, commands):
    answer = []
    for c in commands:
        arr = sorted(array[c[0]-1:c[1]])
        num = arr[c[2]-1]
        answer.append(num)
    return answer

array1 = [1, 5, 2, 6, 3, 7, 4]
com = [[2, 5, 3], [4, 4, 1],[1, 7, 3],[3,7,5]]
# print(solution(array1,com))

