# 2908 - 상수

# 거꾸로 읽기가 핵심인 것 같습니다. 리스트는 [::-1]로 거꾸로 읽기가 가능합니다.

a, b = input().split()

a_ss = a[::-1]
b_ss = b[::-1]

print(a_ss) if a_ss > b_ss else print(b_ss)  # if문 안의 조건이 참이면 if문 전 출력, 거짓이면 else 이후 출력
# if 문을 쓰려다가 좀 더 편한 방법이 없을까 찾아보다가 if-else 삼항연산자라는 방법을 찾아, 적용시켰습니다.
