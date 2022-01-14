numList = [] # 숫자리스트
remList = [] # 나머지를 위한 리스트

for i in range(10):
    numList.append(int(input())) # 10번 input 생성, 삽입

for num in numList:
    rem = num % 42 # 나머지
    if rem not in remList: # 나머지가 나머지리스트에 없으면
        remList.append(rem) # 삽입
    else:
        pass # 아니면 pass

print(len(remList)) # 나머지 리스트 길이가 곧 서로 다른 나머지 수

