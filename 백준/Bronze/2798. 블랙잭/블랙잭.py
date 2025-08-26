# m을 넘지 않으며 가장 가까운 합을 만들기 위해 n장의 카드 중 3장을 뽑아야 함
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers_sum = 0
max_number = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            numbers_sum = numbers[i] + numbers[j] + numbers[k]
            if numbers_sum > m:
                continue
            max_number = max(max_number, numbers_sum)

print(max_number)