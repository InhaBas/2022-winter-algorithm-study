from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(room: list)-> int:
    human = []
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'P':
                human.append([i, j])

    for start in human:
        que = deque([start])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[start[0]][start[1]] = 1

        while que:
            x, y = que.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx <= 4 and 0 <= ny <= 4 and visited[nx][ny] == 0:

                    if distance[x][y] <= 1 and room[nx][ny] == 'O':
                        distance[nx][ny] = distance[x][y] + 1
                        que.append([nx, ny])
                        visited[nx][ny] = 1

                    if distance[x][y] <= 1 and room[nx][ny] == 'P':
                        return 0
    return 1

def solution(place: list)-> list:
    answer = []
    for i in place:
        answer.append(bfs(i))
    return answer