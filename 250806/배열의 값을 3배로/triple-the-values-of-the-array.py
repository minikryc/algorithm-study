lst = []
for i in range(3):
    nums = list(map(int, input().split()))
    lst.append(nums)

for element in lst:
    new_nums = [i * 3 for i in element]
    for new_num in new_nums:
        print(new_num, end = " ")
    print()