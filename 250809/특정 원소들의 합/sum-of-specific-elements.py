numbers = [list(map(int, input().split())) for _ in range(4)]
total = 0
for i in range(4):
    for j in range(4):
        if i >= j:
            total += numbers[i][j]
print(total)