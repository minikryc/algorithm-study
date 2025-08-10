# 내 풀이
n = int(input())
count = 0

count += n // 500
count += (n % 500) // 100
count += ((n % 500) % 100) // 50
count += (((n % 500) % 100) % 50) // 10

print(count)

# 다른 풀이
n2 = int(input())
count2 = 0

coins = [500, 100, 50, 10]
for coin in coins:
    count2 += n2 // coin
    n2 %= coin
print(count2)