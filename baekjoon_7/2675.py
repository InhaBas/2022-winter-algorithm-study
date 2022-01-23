# 2675 - 문자열 반복

TC = int(input())

for i in range(TC):
    num, wrd = input().split()  # split 함수를 통해 공백으로 구분해준다. -> 어차피 나중에 int를 쓰면 되느 굳이 변수를 두 줄에 걸쳐 만들 이유가 없었다...

    text = ''  # 리스트 형식을 쓰면 출력이 이상해 질 것이므로 빈 문자열을 하나 생성성

    for i in wrd: #단어 첫번째부터...
        text += int(num) * i # text에 num번만큼 단어의 첫번째를 반복하여 text에 넣는다.

    print(text) #출력!
