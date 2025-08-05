n = int(input())
number = 1

for i in range(1, n + 1):
    count = 1
    for j in range (1, i + 1):
        if count == i:
            print(number, end = "\n")
            number += 1
        else: 
            print (number, end = " ")
            number += 1
            count += 1