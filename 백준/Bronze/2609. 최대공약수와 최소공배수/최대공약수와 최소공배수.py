a, b = map(int, input().split())

def gcd(a, b):
    while b: 
        a, b = b, a % b
    return a

print(gcd(a, b)) # 최대 공약수
print(a * b // gcd(a, b)) # 최소 공배수