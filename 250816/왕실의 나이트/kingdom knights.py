now = input()
row = int(now[1])
col = int(ord(now[0])) - int(ord("a")) + 1
moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
count = 0

for move in moves:
    new_row = row + move[0]
    new_col = col + move[1]
    if new_row < 1 or new_col < 1 or new_row > 8 or new_col > 8:
        continue
    count += 1
print(count)

