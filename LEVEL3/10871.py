n, x = map(int, input().split())
aList = list(map(int, input().split())) # 수열 a를 이루는 정수 n => List를 만들어라

for i in aList: # aList[0]부터 순회. i 는 실질적 숫자가 될 것
    if i < x:
        print(i, end=" ") # 개행(newline)을 원치 않을 때는 print 함수의 매개변수로 end='' 를 추가해주면 된다.
        # newline in python:
        # https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chandong83&logNo=221160472657

