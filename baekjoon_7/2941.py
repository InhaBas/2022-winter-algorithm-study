#2941 - 크로아티아 알파벳

cro_alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for i in cro_alpa:
    word = word.replace(i, '*') #크로아티아 알파벳 i 가 있다면, *로 대체. 어차피 len으로 세면 되니 형태는 상관 없다.

print(len(word))