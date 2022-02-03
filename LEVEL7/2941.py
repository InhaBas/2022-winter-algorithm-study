cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in cro: # cro 를 순회
    word = word.replace(i, '*') # word 내에 i가 있으면, i를 *로 바꿈
print(len(word)) 