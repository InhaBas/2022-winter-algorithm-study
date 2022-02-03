# 1085 - 직사각형에서 탈출

x, y, w, h = map(int, input().split())

possible_case = []

if x < w - x:
    possible_case.append(x)
else:
    possible_case.append(w - x)

if y < h - y:
    possible_case.append(y)
else:
    possible_case.append(h - y)

print(min(possible_case))