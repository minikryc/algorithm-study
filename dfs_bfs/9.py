n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 좌표의 범위를 벗어나면 False
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 해당 좌표가 방문되지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True # 근처의 0 전부 방문 처리 완료
    
    # 해당 좌표가 방문처리 되어있다면 
    return False 

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
print(count)