n = int(input())
lst_a = set(map(int, input().split()))
m = int(input())
lst_b = list(map(int, input().split()))

for i in lst_b:
    if i in lst_a:
        print(1)
    else:
        print(0)