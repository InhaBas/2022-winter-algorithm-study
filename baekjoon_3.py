# for 문 문제풀이

#1

A = int(input())

for i in range(1,10):
    result = A * i
    print('%d * %d = %d' %(A, i, result))

#2

L = int(input()) #테스트 케이스의 길이

for i in range(L):
    a, b = map(int,input().split()) #두 수 a,b를 입력받아 출력.
    print(a+b)

#3

t = int(input())
len = 0 #빈 변수 하나 설정

for i in range(1,t+1):
    len += i

print(len)

#4
# 잘 이해가 되지 않아 구글링의 도움을 받았습니다...

import sys

a = int(sys.stdin.readline())

for i in range(a):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

#5

n = int(sys.stdin.readline())

for i in range(1,n+1):
    print(i)

#6

n = int(sys.stdin.readline())

for i in range(n, 0, -1):
    print(i)

#7

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print('Case#%d: %d'%(i+1, a+b))

#8

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print('CASE#%d: %d + %d = %d'%(i+1, a, b, a+b))

#9

n = int(sys.stdin.readline())

for i in range(1, n+1):
    print(i * '*')

#10

n = int(sys.stdin.readline())

for i in range(1, n+1):
    print(((n - i) * " ") + (i * '*'))

#11

N, X = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if lst[i] < X:
        print(lst[i], end="")





