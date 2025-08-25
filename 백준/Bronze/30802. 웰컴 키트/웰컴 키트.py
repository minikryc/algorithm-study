n = int(input()) # 참가자 수
sizes = list(map(int, input().split())) # s, m, l, xl, xxl, xxxl
t_set, pen_set = map(int, input().split())

t_set_count = 0
pen_set_count = 0
pen_count = 0

# 옷 세트 카운트
for i in sizes:
    if i == 0:
        continue
    elif t_set > i:
        t_set_count += 1
    else:
        t_set_count += (i // t_set)
        if i % t_set != 0:
            t_set_count += 1
print(t_set_count)

# 펜 세트 카운트
pen_set_count = n // pen_set
pen_count = n % pen_set
print(pen_set_count, pen_count)