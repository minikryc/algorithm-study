def dfs(graph, v, visited):

    # 현재 노드 방문처리
    visited[v] = True
    print(v, end = " ") # depth first search로 방문된 순서대로 노드 출력

    # 현재 노드와 연결된 다른 노드 재귀적 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
        
# 그래프를 2차원 리스틑로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문된 노드 정리용 리스트
visited = [False] * 9

# 1번 노드부터 방문
dfs(graph, 1, visited)