a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a > b :
    print(a)
else :
    print(b)

# reverse() 함수도 이용 가능
# 리스트 변수명[시작 인덱스:종료 인덱스: step] -> 리스트 슬라이싱