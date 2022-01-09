def solution(s: str) -> int:
    if len(s) == 1:
        return 1
    answer = []
    for i in range(1, (len(s)//2) + 1):
        temp = s[:i]
        cnt = 1
        st = ""
        for j in range(i, len(s), i):
            if temp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    st += str(cnt) + temp
                    temp = s[j:i+j]
                    cnt = 1
                else:
                    st += temp
                    temp = s[j:i+j]
                    cnt = 1
        if cnt != 1:
            st += str(cnt) + temp
        else:
            st += temp
        answer.append(len(st))
    return min(answer)