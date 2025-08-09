n = int(input())
lst = [[0] * n for _ in range(n)]

for i in range(n):
    number_inc = 1
    number_dec = n      
    for j in range(n):
        if i % 2 == 0:
            lst[j][i] = number_inc
            number_inc += 1
        else:
            lst[j][i] = number_dec
            number_dec -= 1

for i in range(n):
    for j in range(n):
        print(lst[i][j], end = "")
    print()