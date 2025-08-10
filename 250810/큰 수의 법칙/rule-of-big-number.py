# 내 풀이
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort() # 오름차순 정렬

largest = numbers[n - 1]
second = numbers[n - 2]

quotient = m // (k + 1)
remainder = m % (k + 1) 
result = quotient * (largest * k + second) + remainder * largest
print(result)