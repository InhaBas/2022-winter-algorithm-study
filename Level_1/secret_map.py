import re
def solution(n: int, arr1: list, arr2: list) -> list:
    answer = []
    for i, j in zip(arr1, arr2):
        answer.append(str(bin(i | j)[2:]).rjust(n, '0').replace('1', '#').replace('0', ' '))
    return answer