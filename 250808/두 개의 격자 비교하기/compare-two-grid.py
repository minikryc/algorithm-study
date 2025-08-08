lst_a = []
lst_b = []

n, m = map(int, input().split())

for i in range(n):
    nums_a = list(map(int, input().split()))
    lst_a.append(nums_a)
for i in range(n):
    nums_b = list(map(int, input().split()))
    lst_b.append(nums_b)

for i in range(n):
    for j in range(m):
        if lst_a[i][j] == lst_b[i][j]:
            print(0, end = " ")
        else:
            print(1, end= " ")
    print()