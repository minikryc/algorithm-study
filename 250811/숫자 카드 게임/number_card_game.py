n, m = map(int, input().split())
min_val = 100
max_val = 0
for i in range(n): # 한 줄마다 확인
    numbers = list(map(int, input().split()))
    min_val = 100 # 초기화 필요
    for number in numbers:
        min_val = min(min_val, number)
    max_val = max(max_val, min_val)

print(max_val)