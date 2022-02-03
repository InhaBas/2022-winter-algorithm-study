# 내가 푼 것. 껄껄 누가 봐도 다른 사람들은 이렇게 안풀었을 것 같아서 찾아봄
num = input()
time = 0
for i in num:
    if i in ['A', 'B', 'C']:
        time += 3
    elif i in ['D', 'E', 'F']:
        time += 4
    elif i in ['G', 'H', 'I']:
        time += 5
    elif i in ['J', 'K', 'L']:
        time += 6
    elif i in ['M', 'N', 'O']:
        time += 7
    elif i in ['P', 'Q', 'R', 'S']:
        time += 8
    elif i in ['T', 'U', 'V']:
        time += 9
    elif i in ['W', 'X', 'Y', 'Z']:
        time += 10
print(time)

# searching result
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'] # 위의 난잡한 if 조건들을 일단 리스트로 만들고
a = input() # input값을 받는다
ret = 0 # 이건 시간~
for j in range(len(a)): # a 길이만큼 반복
    for i in dial: # dial 리스트를 순회하는 for문
        if a[j] in i: # 만약에 a[j]가 dial[i] 안에 존재하면
            ret += dial.index(i)+3 # 시간은 인덱스번호에다가 3을 더해준 값이다~ 이말임
print(ret)

# 와 ... 사람들 대단해........
