aList = []

for i in range(9):
    aList.append(int(input())) #input 9번 생성 후 삽입

print(max(aList))
print(aList.index(max(aList)) + 1) # 인덱스 위치 찾았으므로, 위치를 찾을 때는 + 1 해주는 것을 잊지 말자
