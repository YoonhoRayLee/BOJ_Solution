import sys
import math

0 1 2 9 
#1 0 1 2
#2 9 10 11
#3 18 19 20
#5 81 82 84
#6 729 
10000
#0 1 2 3            4*1
#100 101 102 103    4*3
#200 201 202 203
#300 201 202 203

temp = list(map(int, input().split()))
n = temp[0]
k = temp[1]
count = []
count.append(0)
count.append(1)
count.append(3)
index = 1
for i in range(3, n/k + 1):
    count.append(count[i-2] + count [i-1] )
    
arr = []
for i in range (0, k):
    arr.append(i)

for i in range (k, n):



print(arr)
#0 1    1
#100 101 2 *1
#01000 10001 2*2
#10100 10101
#1000000 1000001 2*3
#1000100 1000101
#1010100 1010101
    



