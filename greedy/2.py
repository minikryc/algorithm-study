# 주어진 수 m번 더해 가장 큰수 만들기
# n = array 크기
# m = 덧셈에 사용될수 있는 수의 개수 
# k = 한 수가 연속으로 더해질수 있는 최대 횟수 

# 제일 큰수, 두번째 큰수만 정해놓고 제일 큰수 max번 더하기 사이에 두번째 큰수 한번씩만 끼워넣어 주면 됨

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

numbers.sort() # 배열 오름차순 정렬

first = numbers[n - 1] # 첫번째 제일 큰수
second = numbers[n - 2] # 두번째 제일 큰수

repeat = m // (k + 1) # (first * k + second) 수열 세트가 몇번 들어갈수 있는지
remainder = m % (k + 1) # 완전한 수열 세트가 들어가고 남는 개수

total = repeat * (first * k + second) + remainder * first
print(total)

