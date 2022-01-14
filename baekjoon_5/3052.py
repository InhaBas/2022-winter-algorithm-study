# 3202 - 나머지

lst = []

for i in range(10):

    a = int(input()) % 42

    if a not in lst:  # not을 통해 리스트 안에 해당 값이 있는지 없는지를 매우 손쉽게 확인할 수 있었다!
        lst.append(a)  # 리스트에 없던 값이었으면 리스트에 추가.

print(len(lst))  # 리스트에는 서로 다른 나머지들만 저장되 있을 것이므로 리스트의 길이 = 갯수
