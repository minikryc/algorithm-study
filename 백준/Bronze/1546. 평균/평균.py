n = int(input()) # 과목 개수
scores = list(map(int, input().split()))
m = max(scores)
total = 0

for score in scores:
    new_score = score / m * 100
    total += new_score
print(total / n)