start = input()
col = int(ord(start[0]) - ord('a')) + 1 # 문자 -> 숫자
row = int(start[1]) # 숫자

steps = [(2, 1), (-2, -1), (2, -1), (-2, 1), (1, 2), (-1, -2), (-1, 2), (1, -2)]
count = 0
for step in steps:
    next_col = col + step[0]
    next_row = row + step[1]
    if next_col >= 1 and next_row >= 1 and next_col <=8 and next_row <= 8:
        count += 1
print(count)