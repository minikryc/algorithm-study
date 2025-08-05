n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if (j == i):
            print(i, end = "\n")
        else:
            print(i, end = " ")