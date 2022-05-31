import math
def solution(n,a,b):
    a_num=math.ceil(a/2)
    b_num=math.ceil(b/2)
    count=1
    while True:
        print(a_num, b_num, count)
        if a_num==b_num or a==0 or b==0:
            break
        else:
            a_num=math.ceil(a_num/2)
            b_num=math.ceil(b_num/2)
            count+=1

    return count










# import math
# def solution(n,a,b):
#     a_num = math.ceil(a/2)
#     b_num = math.ceil(b/2)
#     print(a_num, b_num)
#     for _ in range(n):


solution(8,1,3)