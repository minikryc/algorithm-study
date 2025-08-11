n, k = map(int, input().split())
count = 0

while True:
    target = (n // k) * k # n가 k로 나누어 떨어지도록 만들어야 하는 수
    count += (n - target) # n이 target이 되려면 이만큼 -1 연산을 해야함
    n = target # -1 연산 해서 n을 target으로 만들어버림

    if n < k: # n / k가 불가능해지면 반복문 탈출
        break
    n //= k
    count += 1

# -1이 되기까지 마지막으로 남은 수들에 대해 1씩 뺌
count += (n - 1)
print(count)