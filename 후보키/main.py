# 프로그래머스 - 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890


from itertools import combinations


def delete_contained(col_combi: list, candidate_set: tuple):
    i = 0
    while i < len(col_combi):
        if set(candidate_set) & set(col_combi[i]) == set(candidate_set):
            col_combi.pop(i)
        else:
            i += 1


def solution(relation: list):
    col_combis = [list(combinations(range(len(relation[0])), i)) for i in range(1, len(relation[0]) + 1)]
    candidates = set()
    for col_combi in col_combis:
        for candidate in candidates:
            delete_contained(col_combi, candidate)
        try:  # 귀찮으니까 인덱스 에러나는건 무시하기
            for combi in col_combi:
                check_set = {"".join([record[c] for c in combi]) for record in
                             relation}
                if len(check_set) == len(relation):
                    candidates.add(combi)
                    print(candidates)
        except IndexError:
            pass
    return len(candidates)


print(solution([["100", "ryan", "music", "2"],
                ["200", "apeach", "math", "2"],
                ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"],
                ["500", "muzi", "music", "3"],
                ["600", "apeach", "music", "2"]]))
