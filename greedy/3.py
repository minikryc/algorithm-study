# n=행, m=열
# 각 행에서 최소 숫자 뽑고, 그 뽑은 애들중 최대 숫자 출력

n, m = map(int, input().split())
result = 0

for i in range(n): # 한 행씩 살펴보기
    row_list = list(map(int, input().split())) # 한 행의 수들을 리스트화
    smallest = 10001
    for j in row_list:
        smallest = min(smallest, j) # 한 행에서 최소값 추출
    result = max(result, smallest) # 한행의 최소값이랑 현재 설정되어있는 result랑 비교해 max 추출

print(result)