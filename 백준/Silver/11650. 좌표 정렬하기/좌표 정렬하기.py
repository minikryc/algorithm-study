import sys

n = int(input())
input = sys.stdin.readline
dots = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dots.append((x, y))

dots.sort(key=lambda x: (x, y))
print("\n".join(f"{x} {y}" for x, y in dots))