import sys

# 한줄씩 불러오는 input() 재정의
input = sys.stdin.readline
# 입력 뒤 \n 제거
n = int(input().strip())
# set 선언 (list말고 set로 해야 중복 제거됨)
words = set()

# words라는 set에 한 요소씩 추가
for i in range(n):
    words.add(input().strip())

# len(w) 길이 우선 정렬, 다음 사전정의 기준 정렬
sorted_words = sorted(words, key=lambda w: (len(w), w))

print("\n".join(sorted_words))