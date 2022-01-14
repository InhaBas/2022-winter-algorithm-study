# 1110 문제

n = int(input())

num = n
count = 0

while True:
    a = num // 10
    b = num % 10
    c = a + b
    num = b * 10 + c % 10

    count += 1

    if num == n:
        break

print(count) #수학적인 방법으로 풀어보았는데, 두자릿수를 리스트 형태로 만들어 문자열의 방식으로도 푸는 방법이 있을 것 같다. 나중에 해당 방식으로 다시 한 번 풀어보겠습니다!
