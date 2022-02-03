n = int(input())

for i in range(n):
    count, word = input().split()
    for w in word:
        print(w * int(count), end='')
    print()


