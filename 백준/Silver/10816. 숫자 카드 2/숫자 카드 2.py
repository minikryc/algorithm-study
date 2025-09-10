import sys

input = sys.stdin.readline

n = int(input())
own_cards = list(map(int, input().split()))
m = int(input())
given_cards = list(map(int, input().split()))

dict = {}
for i in own_cards:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for i in given_cards:
    if i in dict:
        print(dict[i], end=" ")
    else:
        print(0, end=" ")