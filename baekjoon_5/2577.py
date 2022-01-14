# 2577 숫자의 개수

a = int(input())

b = int(input())

c = int(input())

aa = str(a * b * c)  # 리스트로 분해해서 세려면 숫자열보다는 문자열이 더 편한 것 같다.

num_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0~9까지의 리스트

for i in range(len(aa)):  # aa의 값을 분해해서 각 자릿수별로, 각 갯수를 세려면? -> 일단 aa의 자릿수를 다 세는 반복문이 가장 이상적일 듯 하다.
    for o in range(10):  # 어차피 0~9중 하나의 정수일테니...
        if int(aa[i]) == o:  # aa는 문자열이므로 숫자로 바꿔 준 뒤 aa의 i번째 수가 어떤 숫자인지 셈. 맞으면...
            num_lst[o] += 1  # num_lst의 j번째 숫자(0부터 9까지)의 갯수를 하나 더함.

for i in range(10):
    print(num_lst[i]) # num_lst에서 한번에 하나씩 뽑아서 print.
