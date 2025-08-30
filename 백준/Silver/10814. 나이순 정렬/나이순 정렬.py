import sys

n = int(input())
input = sys.stdin.readline
members = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    members.append((age, name)) # 리스트에 튜플로 넣기 가능

members.sort(key=lambda x: x[0]) # sort()는 리스트의 아이템 하나씩 순차적으로 key 함수에 넣음

print("\n".join(f"{age} {name}" for age, name in members))