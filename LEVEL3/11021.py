import sys

t = int(sys.stdin.readline())


for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d" %(i+1, a+b))

# %d(정수), %s(문자열), %f(실수)