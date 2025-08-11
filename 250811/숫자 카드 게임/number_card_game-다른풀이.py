n, m = map(int, input().split())
max_val = 0

for i in range(n): # 한 줄마다 확인
    numbers = list(map(int, input().split()))
    min_val = min(numbers)
    max_val = max(max_val, min_val)

print(max_val)