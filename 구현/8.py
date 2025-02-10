n, m = map(int, input().split())
x, y, direction = map(int, input().split()) # x좌표, y좌표, 방향
game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split()))) # 주어진 게임 맵
visited_map = [[0] * m for _ in range(n)] # 방문한 위치 기록용 맵
visited_map[x][y] = 1
dx = [-1, 0, 1, 0] # 북 동 남 서 
dy = [0, 1, 0, -1] # 북 동 남 서 
count = 1 # 방문한 칸의 수
turn_count = 0    

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:
    # 왼쪽으로 돌기
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 돌았을때 안가본 칸 존재 : 현 방향으로 한칸 전진
    if visited_map[nx][ny] == 0 and game_map[nx][ny] == 0: # 회전한 위치로 전진 안가봤고 육지이면
        visited_map[nx][ny] = 1 # 이동했으니깐 가본걸로 체크
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue # 바로 다음 루프 실행

    # 돌았을때 가본 칸 존재 : continue
    else: # 다 가봤거나 바다이면
        turn_count += 1 
        # 현위치에서 돌기만한 횟수 == 4 : 현 방향 기준 뒤로 한칸, 왼쪽 돌기로 돌아가기
        if turn_count == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 이동 가능하면:
            if game_map[nx][ny] == 0:
                x = nx
                y = ny
                turn_count = 0
            # 뒤로 이동 안되면
            else: 
                break # 반복문 즉시 종료

print (count)