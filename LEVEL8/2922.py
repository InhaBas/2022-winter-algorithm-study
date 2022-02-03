n = int(input())

count = 1
sumNum = 1

while True:
    if n == 1:
        print('1')
        break
    else:
        sumNum += count * 6
        if n <= sumNum:
            print(count + 1)
            break
        else:
            count += 1

'''
지나는 방의 수는 1 , 7, 19, 37, 61 ... 지날 때마다 1개씩 증가

=> 6씩 증가하는 계차 수열이다.

따라서 count에 6을 곱함, sumNum에 더해 N과 비교하여 N이 sumNum보다 작거나 같을 경우 count+1을 출력
'''
