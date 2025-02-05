# 시뮬레이션

n = int(input()) # 공간의 크기 n x n
steps = input().split() # 움직임들을 배열로 받음

x, y = 1, 1
move_types = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for step in steps:
    for i in range(len(move_types)):
        if step == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n: # 부적합 움직임은 count 안하고 다음 루프로 넘겨버림
        continue

    x, y = nx, ny

print(x, y)