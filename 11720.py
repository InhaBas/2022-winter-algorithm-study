n = int(input())
num = list(input()) # list형 문자열
sum = 0
for i in num:
    sum += int(i) # int형으로 전환
print(sum)