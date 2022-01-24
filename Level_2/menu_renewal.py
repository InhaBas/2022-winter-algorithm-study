from itertools import combinations
from collections import Counter

def solution(orders: list, course: list) -> list:
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) and max(counter.values()) != 1:
            answer += [''.join(menu) for menu in counter if counter[menu] == max(counter.values())]

    return sorted(answer)