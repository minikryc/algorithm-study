# n이 1이 될때까지 n-1 혹은 n//k를 계속 수행
# 결과값 : 최소 연산 횟수

n, k = map(int, input().split())

count = 0
while (n != 1):
    if n % k == 0: # n이 나누어 떨어지면
        n = n // k
        count += 1
    else: # n이 나누어 떨어지지 않으면
        n -= 1
        count += 1

print(count)