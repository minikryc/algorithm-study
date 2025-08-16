n, m = map(int, input().split())
x, y, direction = map(int, input().split()) 
visited = [[0] * m for _ in range(n)] # n*m 크기로 방문맵 초기화
visited[x][y] = 1 # 현 좌표 방문 처리

# 맵 입력받기
arr = []
for i in range (n):
    rows = list(map(int, input().split()))
    arr.append(rows)

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 함수 정의
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 게임 메뉴얼
count = 1
turn_time = 0
while True:
    # 1. 왼쪽 방향으로 회전
    turn_left()
    nx = x + dx[direction] # 임시 전진
    ny = y + dy[direction]

    # 1-1. 0 존재하면 왼쪽으로 한칸 전진
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx # 전진 확정
        y = ny
        count += 1
        turn_time = 0 # 전진 했으니깐 회전 횟수 초기화
        continue
    # 1-2. 1 존재하면 1단계로
    else:
        turn_time += 1

    # 2. 네 방향 모두 1이면 방향유지하고 한칸 뒤로가 1단계로
    if turn_time == 4:
        nx = x - dx[direction] # 임시 후진
        ny = y - dy[direction]
    # 2-1. 한칸 뒤가 0이면 뒤로 한칸 가고 1단계로
        if visited[nx][ny] == 0 and arr[nx][ny] == 0:
            x = nx # 후진 확정
            y = ny
    # 2-2. 한칸 뒤가 1이면 움직임 정지 (게임 끝)
        else:
            break 
        turn_time = 0

print(count)