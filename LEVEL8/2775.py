T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    people = [ i for i in range(1, n+1)]
    for __ in range(k):
        for j in range(1,n):
            people[j] += people[j-1]
    print(people[-1])


'''
문제 이해를 못해서 구글링함...
list를 for 문으로도 만들 수 있구만
문제 이해:
3층 3호에 살고자 한다. 3층 3호에 살려고 한다면 2층 1호, 2층 2호, 2층 3호에 사는 사람들의 합만큼 3층 3호에 데리고 살아야 한다.
3층 2호 => 2층 1호, 2층 2호에 사는 사람들의 합만큼
3층 3호 => 3층 2호에 데리고 살아야 하는 인원 + 2층 3호에 데리고 살아야 하는 인원이 된다.
'''
