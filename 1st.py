#1
print("Hello World!")

#2
print("강한친구 대한육군\n"*2)

#3

#a = int(input())
#b = int(input())
#if 0 < a < 10 and 0 < b < 10:
#    print(a+b)

A, B = input().split()
print(int(A)+int(B))

# 주석과 답의 차이점은?
#split -> 문자열 함수 / 따라서 int형으로 재지정 필요

# 9 사칙연산
a, b = map(int, input().split()) # map 함수는 결과 모두 int형으로 반환해라 라는 뜻
print(a+b)
print(a-b)
print(a*b)
print(a//b) # 몫 부분만
print(a % b) # 나머지

# 10
A, B, C = map(int, input().split()) #
print((A+B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

# 11
#A, B = input(), input()
#print(A * int(B[2]))
#print(A * int(B[1]))
#print(A * int(B[0]))
#print(A * B)
#런타임 에러가 뜸 왜 슬라이싱은 안 되는지

a = int(input())
b = int(input())
print(a*(b%10))
print(a*int((b%100-b%10)/10))
print(a*(b//100))
print(a*b)
