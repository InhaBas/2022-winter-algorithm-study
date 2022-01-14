# 1차원 배열 - 10818 문제.
import sys

lst = []

n = int(sys.stdin.readline())

a = sys.stdin.readline().split()  # split 함수로 공백으로 각각 구분, 리스트의 형태로 저장. split 함수는 문자열만 쪼개기가 가능하므로 int는 불가.

for i in range(n):
    lst.append(int(a[i]))  # a의 값이 문자열이므로 숫자로 변경

print(min(lst), max(lst))  # 리스트 안에서 최소, 최대 값 출력
