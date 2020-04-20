import sys

def funcCnt(s):
    if len(tree[s])>0:
        for i in range(len(tree[s])):
            if tree[s][i] != delNode:
                funcCnt(tree[s][i])
            else:
                if len(tree[s]) == 1:
                    cnt+=1
    else:
        cnt +=1

N = int(input())
if N>50:
    exit()
arr = list(map(int, sys.stdin.readline().strip().split()))
delNode = int(input())
tree = [[0] for i in range(N)]
root = []
cnt = 0
for i in range(N):
    if(arr[i] != -1):
        tree[arr[i]].append(i)
    else:
        root.append(i)
    for i in range(len(root)):
        if delNode != root[i]:
            funcCnt(root[i])
print(cnt)