m = int(input())
n = int(input())

prime = []

for i in range(m, n + 1):
    check_prime = True
    for j in range(2, i):
        if i % j == 0:
            check_prime = False
            break
    if i == 1:
        check_prime = False
    if check_prime == True:
        prime.append(i)

prime_sum = 0
for i in range(len(prime)):
    prime_sum += prime[i]
if len(prime) < 1:
    print(-1)
else:
    print(prime_sum)
    print(prime[0])