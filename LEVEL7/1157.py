word = input().upper() # input 받아!
word_list = list(set(word)) # word 중복 없이 list 만들어!

cnt = [] # 몇번 쓰였는지 정의할 빈 리스트 만들어!

for i in word_list: # word에서 사용된 알파벳을 순회해
    count = word.count(i) # word에서 사용된 알파벳이 몇번 사용되었는지 count에 정의하고
    cnt.append(count) # cnt 리스트에 넣어!

if cnt.count(max(cnt)) >= 2: # 만약 가장 많이 사용된 알파벳의 개수가 1을 초과한다면
    print("?") # ?를 출력하고
else: #그게 아니라면
    print(word_list[(cnt.index(max(cnt)))]) # 가장 많이 사용된 알파벳의 위치(인덱스)를 찾아 알파벳을 출력해




# 왕 어렵다 정말