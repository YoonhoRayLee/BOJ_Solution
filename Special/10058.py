import sys
import math


n, d = list(map(int,sys.stdin.readline().strip().split()))
sensors = [[0,0]]
dp=[]
dp.append(0)
group = []
group.append(0)
for i in range(n):
    sensors.append(list(map(int, sys.stdin.readline().strip().split())))
for i in range(1,n+1):
    tmp = []
    for j in range(1,n+1):
        if i == j:
            continue
        else:
            difx = sensors[j][0] - sensors[i][0]
            dify = sensors[j][1] - sensors[i][1]
            dist = math.sqrt(pow(difx,2)+pow(dify,2))      
            distmp.append(dist)
            if dist <= d:
                tmp.append(j)
    tmp = list(set(tmp))        
    group.append(tmp)
    distance.append(distmp)



for i in range(n+1):
    print(distance[i])
print(group)