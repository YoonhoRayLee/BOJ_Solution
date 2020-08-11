#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1068

import sys

class node():
    def __init__(self):
        self.parents = None
        self.child = []

N = int(input())
if N>50:
    exit()
arr = list(map(int, sys.stdin.readline().strip().split()))
delNode = int(input())
tree = [0]*N
root = 0
for i in range(N):
    #트리 내에 노드 생성 및 부모 노드 지정
    if tree[i] == 0:
        tree [i] = node()
    tree[i].parents = arr[i]

    if tree[arr[i]] == 0:
        tree[arr[i]] = node()

    #루트 노드의 인덱스 root에 저장
    if arr[i] == -1:
        root = i
    #루트 노드 이외의 노드들은 부모 노드의 자식 리스트에 추가
    else:
        tree[arr[i]].child.append(i)

leaf = 0

#삭제할 노드의 부모 노드가 루트 노드가 아니라면 
if tree[delNode].parents != -1:
    tree[tree[delNode].parents].child.remove(delNode)
#삭제할 노드의 부모노드가 루트 노드라면
else:
    tree[delNode].child = []
    leaf = -1

q = tree[root].child

while q:
    Next=[]
    for v in q:
        if len(tree[v].child) == 0:
            leaf +=1
        for u in tree[v].child:
            Next.append(u)
    q = Next
if leaf == -1:
    print(leaf+1)
elif leaf == 0:
    print(1)
else:
    print(leaf)