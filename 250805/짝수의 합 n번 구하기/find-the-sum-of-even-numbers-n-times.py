n = int(input())
for i in range(n):
    sum = 0
    a, b = map(int, input().split())
    for j in range (a, b + 1): #2 4 6 8 10 12 14 16 18 20
        if j % 2 == 0:
            sum += j
    print(sum)