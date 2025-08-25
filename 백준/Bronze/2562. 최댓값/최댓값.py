max = 0
order = 0
for i in range(9):
    num = int(input())
    if num > max:
        max = num
        order = i + 1

print(max)
print(order)