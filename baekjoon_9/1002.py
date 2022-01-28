# 1002 - 터렛
# 원 모양으로 거리를 구하니 겹치는 점은 0개, 1개, 2개, 무한대 중 하나이다.


t = int(input())

for i in range(t):
    x1, y2, r1, x2, y1, r2 = map(int, input().split())

    dis = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5  # 두 점 사이의 거리

    rs = [r1, r2, dis]

    m = max(rs)  # 최댓값 제거

    rs.remove(m)

    print(-1 if (r1 == r2) and dis == 0 else 1 if (dis == r1 + r2) or m == sum(rs) else 0 if dis > r1 + r2 or m > sum(
        rs) else 2)

    # 내부에서 만나는 점, 외부에서 만나는 점 등을 식으로 정리
