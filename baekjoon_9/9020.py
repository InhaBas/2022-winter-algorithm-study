# 9020 - 골드바흐의 추측
# 2보다 큰 짝수는 소수의 합으로 나타낼 수 있다는 추측.
# for 문으로 만들었다가 망하고, 이후 더 생각하다가 정말 모르겠어서 인터넷의 도움을 받았습니다.

nums = {i for i in range(2, 10001) if i % 2 == 1 or i == 2}  # 소수 리스트 만드는건 재활용

for holsu in range(3, int(10001 ** 0.5) + 1, 2):  # holsu는 3부터 시작해서 246913의 제곱근까지의 홀수들
    nums -= {i for i in range(2 * holsu, 10001, holsu) if i in nums}  # 2와 모든 홀수에서 각 수의 제곱들을 빼서 소수만 남게

n = int(input())

for i in range(n):

    input_num = int(input())  # 짝수를 입력받는다

    for j in range(input_num // 2, 1, -1):  # 입력받은 수의 절반을, 큰 수부터, 1씩 줄여가며 더한다.

        if j and input_num - j in nums: #두 수의 차이가 가장 적은 소수 두개를 출력하는 과정
            print(j, input_num - j)
            break
