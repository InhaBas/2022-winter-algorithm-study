#1
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: # 순서
        break
    print(a+b)

#2
while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a + b)

# try except문: try ~~ except [발생 오류]: ~~~
# try 수행 중에 오류가 발생하면 except문 수행되며, []안의 내용은 생략 가능하다.
# 점프투파이썬에 따르면, try finally 문도 있다. finally문은 사용한 리소스를 close 해야 할 때 많이 사용한다.
# https://wikidocs.net/30 확인(오류에 대한 예외 처리 방법)


#3
n = int(input()) # input()은 어떤 것을 다 받는지 str로 입력된 후 list []로 저장한다.
num = n
cle = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    cle = cle + 1
    if (num == n):
        break
print(cle)

# 3번 풀이의 번외로 str형을 이용한 방법 있음. https://wook-2124.tistory.com/222
# while 1: -> 무한 반복으로서 while True랑 동일