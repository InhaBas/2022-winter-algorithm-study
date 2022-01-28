# 11653 - 소인수분해

n = int(input())

i = 2 #최소의 소수인 2 입력

while n != 1:
    #for i in range(2, n+1): 여기다 for문을 넣으면 i 값이 그냥 증가해서 반복이 불가능했습니다...
    if n % i != 0:
       i += 1
    else:
        print(i)
        n /= i
