N = int(input())
num_list = list(map(int, input().split()))

def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

count = 0
for i in num_list:
    if prime(i):
        count += 1

print(count)