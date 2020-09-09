from collections import deque
import sys

n = int(input())
# 원하는 순서의 수열
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = deque(arr)
stack, answer, ans = [], [], []
idx, arrIdx = 1, 0
while True:
    if arrIdx >= n:
        break
    tmp = arr[arrIdx]
    if len(ans) == n:
        break
    # 원하는 값과 같지 않으면 push
    if idx != tmp:
        stack.append(idx)
        answer.append('+')
        idx += 1
    # 원하는 값과 같으면 push and pop
    else:
        answer.append('+')
        answer.append('-')
        ans.append(tmp)
        arrIdx += 1
        while True:
            if len(stack) == 0:
                break
            if arr[arrIdx] == stack[-1]:
                ans.append(stack.pop())
                answer.append('-')
                arrIdx += 1
            else:
                if stack and stack[-1] > arr[arrIdx]:
                    print('NO')
                    sys.exit()
                break 
        idx += 1  
for i in answer:
    print(i)