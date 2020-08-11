import sys

n = int(input())
m = int(input())
friends = []
a = []
b = []
friends = [[sys.maxsize]*(n+1) for i in range(n+1)]
realFriends = []
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 1:
        friends[a][b] = 1
        realFriends.append(b)
    elif b == 1:
        friends[b][a] = 1
        realFriends.append(a)
    else:
        if realFriends.count(a)>0:
            friends[a][b] = 1
        elif realFriends.count(b)>0:
            friends[b][a] = 1
        else:
            friends[a][b] = 2

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if friends[i][k]+friends[k][j] <= 3:
                realFriends.append(j)
realFriends = list(set(realFriends))
print(realFriends)
print(len(realFriends))
#5 6 7 9
#10 3 8 