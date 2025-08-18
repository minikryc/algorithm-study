from collections import deque

def bfs(graph, start, visited):

    # queue 구현
    queue = deque([start]) 

    # 현재 노드 방문 처리
    visited[start] = True

    # queue가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end = " ")

        # 해당 원소와 연결된, 아직 방문처리 안된 노드들을 큐에 삽입
        for i in graph[v]:
            if visited[i] == False: # if not visited[i] 이거랑 같음
                queue.append(i)
                visited[i] = True

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

visited = [False] * 9

bfs(graph, 1, visited)