#1
a = int(input())

for i in range(1, 10):
    print(a, "*", i, "=", a*i)

#2
a = int(input())
for _ in range(a): # 언더바 선언
    b, c = map(int,  input().split())
    print(b + c)

#3
n = int(input())
sum = 0
for i in range(n+1):
    sum = sum + i
print(sum)

#4
import sys

inp = int(input())
for i in range(inp):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

#5
inp = int(input())
sum = 0
for i in range(inp):
    sum = sum + 1
    print(sum)

#6
inp = int(input())
for i in range(inp):
    print(inp-i)

#7
a = int(input())
for i in range(a): # 언더바 선언
    b, c = map(int,  input().split())
    print("Case #%d: %d" %(i+1, b+c)) #

#8
a = int(input())
for i in range(a): # 언더바 선언
    b, c = map(int,  input().split())
    print("Case #%d: %d + %d = %d" %(i+1, b, c, b+c))

#9
a = int(input())
for i in range(1, a+1): #
    print("*" * i)

#10
a = int(input())
for i in range(1, a+1):
    print(" " * (a-i) + "*" * i) # 문자열 합칠 때도 +

#11
n, x = map(int, input().split())
num = list(map(int, input().split())) # 리스트 형으로 입력받음
for i in range(n):
    if num[i] < x:
        print(num[i], end = " ") # end = " " 로 한 칸씩 띄어서 출력