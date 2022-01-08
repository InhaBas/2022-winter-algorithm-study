#1

A = int(input())

B = int(input())

if A > B:
    print('>')
elif A == B:
    print('==')
elif A < B:
    print('<')

#2

A = int(input('test result:'))

if 100 >= A >= 90:
    print('A')
elif 90 > A >= 80:
    print('B')
elif 80 > A >= 70:
    print('C')
elif 70 > A >= 60:
    print('D')
else:
    print('F')

#3

A = int(input())

if A // 4 == 0 and A % 100 !=0:
    print('1')
elif A // 400 == 0:
    print('1')
else:
    print('0')

#4

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

#5

H, M = map(int, input().split())

if M >= 45:
    print(H, M - 45)
elif H == 0:
    print(23, 60 + (M - 45))
else:
    print(H-1, 60 + (M - 45))