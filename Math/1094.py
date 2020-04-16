#gotta fix

sL = 64
stack = []
stack.append(sL)
X = int(input())
cnt = 0

if sL > X:
    while True:
        cnt += 1
        sL = stack.pop()
        for i in range(2):
            stack.append(sL/2)
        if sum(stack) >= X:
            stack.pop()
        print(stack)
        tmp = sum(stack) - X
        if stack.count(tmp) >= 1 or sum(stack) - X == 0:
            break
elif sL == X:
    cnt = 1

print(cnt)
