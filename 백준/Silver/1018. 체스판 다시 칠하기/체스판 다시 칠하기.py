import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

# 검흰 번갈아며 확인
def repaint(x, y): # x, y = 시작 좌표
    w_start = 0 # 첫번째(x, y)를 화이트로 시작했을때, 다시 칠해야 하는 수
    b_start = 0 # 첫번째(x, y)를 블랙으로 시작했을때, 다시 칠해야 하는 수
    for i in range(8):
        for j in range(8):
           now = board[x + i][y + j] # 현재 보고 있는 좌표
           # i + j가 짝수면 첫번째(x, y)랑 같은 컬러로
           if (i + j) % 2 == 0:
              if now != "W": w_start += 1 # 첫번째(x, y)를 화이트라고 했을때
              if now != "B": b_start += 1 # 첫번째(x, y)를 블랙이라고 했을때
            # i + j가 홀수면 첫번째(x, y)랑 다른 컬러로
           else:
              if now == "W": w_start += 1 # 첫번째(x, y)를 화이트라고 했을때
              if now == "B": b_start += 1 # 첫번째(x, y)를 블랙이라고 했을때
    return min(w_start, b_start)


total = 64

# 몇번째부터 8*8 크기로 확인할수 있는지
for i in range(n - 7):
    for j in range(m - 7):
        total = min(total, repaint(i, j))
print(total)