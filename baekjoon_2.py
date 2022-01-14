# 1

a = int(input())

b = int(input())

if a > b:
    print('>')
elif a == b:
    print('==')
elif a < b:
    print('<')

# 2

a = int(input('test result:'))

if 100 >= a >= 90:
    print('A')
elif 90 > a >= 80:
    print('B')
elif 80 > a >= 70:
    print('C')
elif 70 > a >= 60:
    print('D')
else:
    print('F')

# 3

a = int(input())

if a // 4 == 0 and a % 100 != 0:
    print('1')
elif a // 400 == 0:
    print('1')
else:
    print('0')

# 4

x, y = map(int, input().split())
# 솔직히 map 함수의 사용법을 아직 잘 모르겠습니다. int(input())을 x,y에 두 줄에 걸쳐 할당하는게 더 직관적이긴 하나 map 함수를 이용하는게 더 깔끔해 보입니다.

if x > 0 and y > 0:
    print("1")
elif x < 0 < y:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')

# 5

h, m = map(int, input().split())

if m >= 45:
    print(H, M + 15)
elif h == 0:
    print(23, M + 15)
else:
    print(H - 1, M + 15)
