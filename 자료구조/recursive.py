# recursive 함수 : 자기 자신을 다시 호출하는 함수
#   - 종료조건 반드시 명시해야 함
#   - 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것
#   - 반복문보다 훨씬 간결

def recursive_func(i):
    if i == 3:
        return # 아무것도 반환하지 않고, 함수를 종료 (reutnr == return None)
    print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
    recursive_func(i + 1)
    print(i, "번째 재귀 함수를 종료합니다.")
recursive_func(1)

def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * factorial(n - 1)
print(factorial(4))