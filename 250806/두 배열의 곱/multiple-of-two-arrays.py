lst_a = []
lst_b = []

for i in range(3):
    nums_a = list(map(int, input().split()))
    lst_a.append(nums_a)
space = input()
for i in range(3):
    nums_b = list(map(int, input().split()))
    lst_b.append(nums_b)

for i in range(3):
    for j in range(3):
        print(lst_a[i][j] * lst_b[i][j], end = " ")
    print()