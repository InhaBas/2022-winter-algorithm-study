# 2562번 - 최댓값.

lst = []

for i in range(9):
    lst.append(int(input()))  # 9 개의 자연수를 입력하는 과정

i = 0

while True:
    if lst[i] == max(lst):  # 인덱스를 통한 숫자의 위치 세기
        break
    i += 1

print(max(lst))
print(i + 1)  # 인덱싱은 0부터 시작하므로 1을 더해야 정확이 몇 번쨰 수인지 알 수 있다.
