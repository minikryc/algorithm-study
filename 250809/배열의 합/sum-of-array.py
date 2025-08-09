numbers = []
for i in range(4):
    nums = list(map(int, input().split()))
    numbers.append(nums)

for i in range(4):
    sum = 0
    for j in range(4):
        sum += numbers[i][j]
    print(sum)