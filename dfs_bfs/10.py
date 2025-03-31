from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동 : 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # queue가 빌때 까지 반복
    while queue:
        # 방문한 노드를 x, y 값으로 설정하고 큐에서 뽑음
        x, y = queue.popleft()

        # 상 하 좌 우 칸 각각 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # grid의 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 해당 위치에 괴물 있으면 무시
            if graph[nx][ny] == 0:
                continue
            # 새로 이동한 해당 위치가 길이면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
        
    # 마지막으로 방문한 노드의 값 반환
    return graph[n - 1][m - 1] 
    
print(bfs(0, 0))