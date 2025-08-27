n, k = map(int, input().split())
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(int(factorial(n) / factorial(k) / factorial(n - k)))