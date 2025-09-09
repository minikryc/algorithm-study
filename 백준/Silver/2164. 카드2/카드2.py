from collections import deque

n = int(input())
queue = deque()
for i in range(1, n+1): # queue = deque(range(1, n+1))이랑 같은 표현
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)
print(queue[0]) 