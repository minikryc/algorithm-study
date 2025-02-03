# 500, 100, 50, 10원짜리 동전 무한개
# 거스름돈 n = 1260원
# 거슬러줘야 할 동전 최소 개수 ?개 (항상 10의 배수)

n = 1260
count = 0
coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n = n % coin
print(count)