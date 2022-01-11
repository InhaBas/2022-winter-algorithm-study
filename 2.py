#1
a, b = map(int, input().split()) # 각각 input이랑 map이랑 무슨 차이인지
if a > b:
    print(">")
elif a < b:
    print("<")
else: print("==")

#2
a = int(input())
if a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >= 60:
    print("D")
else: print("F")

#3
a = int(input())
if (a%4==0 and a%100 != 0) or a%400 == 0:
    print("1")
else: print("0")

#4
a = int(input()) # 왜 얘는 split 함수가 안 되는지
b = int(input())
if a >0 and b>0:
    print("1")
elif a < 0 and b > 0:
    print("2")
elif a < 0 and b < 0:
    print("3")
else: print("4")

#5
a, b = map(int, input().split())
if b >= 45:
    print(a, b-45)
elif a > 0 and b < 45:
    print(a-1, b+15)
else: print(23, b+15)