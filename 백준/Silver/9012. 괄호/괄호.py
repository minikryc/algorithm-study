t = int(input())
for i in range(t):
    stack = []
    s = input()
    is_vps = True
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else: 
                is_vps = False
                break
    if stack:
        is_vps = False
    print("YES" if is_vps else "NO")