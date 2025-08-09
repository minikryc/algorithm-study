n = int(input())
count = 0
numbers = []
for i in range(1, n + 1):
    numbers.append(i)
while count < n:
    for i in range(n):
        print(numbers[i], end = "")
    count += 1
    numbers.reverse()
    print()