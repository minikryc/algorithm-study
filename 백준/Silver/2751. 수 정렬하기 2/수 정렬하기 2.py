import sys

input = sys.stdin.readline
n = int(input().strip())
nums = []

for i in range(n):
    nums.append(int(input().strip()))

nums.sort()
print("\n".join(map(str, nums)))