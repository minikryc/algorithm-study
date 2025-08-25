n = int(input())
count = 0
nums = list(map(int, input().split()))

for i in nums:
    div_count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            div_count += 1
    if div_count == 2:
        count += 1
print(count)