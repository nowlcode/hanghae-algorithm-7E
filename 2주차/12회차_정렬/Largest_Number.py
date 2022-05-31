from typing import List


def largestNumber(nums: List[int]) -> str:
    answer = ''
    first_char = []
    for n in nums:
        first_char.append(str(n))
    print(sorted(first_char, reverse=True))
    for first in first_char:

    #규칙:

#[9,5,3,3,3] <-str
largestNumber([3,30,34,5,9])