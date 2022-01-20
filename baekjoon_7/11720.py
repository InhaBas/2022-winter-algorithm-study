# 11720 - 숫자의 합


a = int(input())

# print(sum(map(int, input()))) 가능은 하지만 이러면 a의 의미가 너무 없는것 같아서...

input_nums = input() #값을 입력받는다

total = 0 #합을 담아줄 바구니

for i in range(a):
    total += int(input_nums[i]) # 문자열은 리스트의 속성도 가지므로 인덱싱을 통해 더해준다. 물론 int로 숫자열로 바꾼 뒤에.

print(total)


