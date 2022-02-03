# 3009 - 네 번째 점

x_lst = [0 for i in range(3)]
y_lst = [0 for i in range(3)]  # [0, 0, 0]

for i in range(3):
    x_lst[i], y_lst[i] = map(int, input().split())

for i in range(3):
    if x_lst.count(x_lst[i]) == 1:  # 축에 평행한 직사각형이므로 x, y좌표중 하나만 나온게 마지막 점의 좌표이다.
        x_a = x_lst[i]

    if y_lst.count(y_lst[i]) == 1:
        y_a = y_lst[i]

print(x_a, y_a)
