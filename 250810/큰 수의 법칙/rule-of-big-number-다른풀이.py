# 다른 풀이
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort() # 오름차순 정렬

largest = numbers[n - 1]
second = numbers[n - 2]

# 가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k # 메인 세트 계산의 횟수 * 가장 큰 수의 개수
count += m % (k + 1) # 메인 세트에 못든 나머지 계산의 횟수

result = 0
result += (count) * largest
result += (m - count) * second
print(result)