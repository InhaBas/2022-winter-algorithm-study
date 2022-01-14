n = int(input())
aList = list(map(int, input().split()))

sortList = sorted(aList)
# 정렬 후 제일 작은 건 최솟값, 제일 큰건 최댓값임. n-1을 해야 맨 마지막 원소 찾기 가능함
print(sortList[0], sortList[n - 1])


