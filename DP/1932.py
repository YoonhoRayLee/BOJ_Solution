import sys

N = int(input())

dp = []
dp.append(0)
arrTri = []
for i in range(N):
    tempArr = list(map(int, sys.stdin.readline().strip().split()))
    arrTri.append(tempArr)

dp.append(arrTri[0])