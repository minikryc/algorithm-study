import sys

input = sys.stdin.readline
N = int(input().strip())
words = set()  # 중복 제거

for _ in range(N):
    words.add(input().strip())

# 길이 기준 정렬, 같은 길이면 사전순 정렬
sorted_words = sorted(words, key=lambda w: (len(w), w))

print("\n".join(sorted_words))