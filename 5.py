#1
n = int(input())
list = list(map(int, input().split()))
print(min(list), max(list))

#2
list = []
for i in range(9): # 리스트 생성 후 append 함수로 input 추가하기
    list.append(int(input()))
print(max(list))
print(list.index(max(list)) + 1)

#3
a = int(input())
b = int(input())
c = int(input())
d = list(str(a * b * c))
for i in range(10):
    print(d.count(str(i)))
     # i 이용해서 함 -> count 함수는 str형에만 사용 가능

#4
list = []
for _ in range(10):
    a = int(input())
    list.append(a % 42)
list = set(list)
print(len(list))
#set 함수는 중복을 제거하기 위한 함수이다 -> 서로 다른 나머지를 출력하기 위함

#5
n = int(input())
list = list(map(int, input().split()))
max = max(list)

for i in range(n):
    list[i] = list[i] / max * 100
print("%.2f" % (sum(list) / n))

#6
n = int(input())
for _ in range(n):
    cnt = 0
    sum = 0
    a = list(input())
    for i in a:
        if i == 'O':
            cnt = cnt + 1
            sum = sum + cnt
        else:
            cnt = 0
    print(sum)

# 푸는 방법
# O일 때, 연속하여 몇 번 O가 들어왔는지 카운트한다.
# O일 때, 임의의 변수에 카운트한 수를 더한다.
# X일 때, 카운트한 수를 0으로 초기화 한다.

#7
c = int(input())
for _ in range(c):
    list = list(map(int, input().split()))
    avr = sum(list[1:]) / list[0]
    cnt = 0
    for i in list[1:]:
        if i > avr:
            cnt += 1
    per = (cnt / list[0]) * 100
    print(f'{per: .3f}%')
#    print('%.3f' % per + '%')