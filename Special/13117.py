#참가자들에는 1부터 N번까지 번호가 매겨져 있는데, 그 중 1번 참가자인 태현이는 참가자들이 가위/바위/보를 낼 확률을 미리 알아내었다! 
#1등부터 N등까지 상품이 다양하지만 태현이가 원하는 상품은 K등을 했을 때 얻을 수 있다. 
4#태현이가 원하는 상품을 얻을 확률을 구하여라.

#태현이 1등(1번 참가자)
# 가위 바위  보
# 0.5 0.5 0.0
# 0.5 0.0 0.5
# 0.0 0.5 0.5

1 2 3 4 5 6 7


1 2 3

1 / 2 3 -> (3가지)  = (0.125)
1 2 / 3(3가지) -> 1 / 2(3가지) = (0.125) * (0.25+0.25) = 0.0625
 = 0.125 + 0.0625 = 0.1875 =  3/16

12가지

무승부
셋다 같은거 (3가지) (0)
1 / 2 / 3 -> (0.25)
-> 1/4 * 3/16 = 3/64





=> 3/16 + 9/64 = 12 + 9 / 64 = 21/64


import sys
import math
#n명 가위바위보 무승부 경우의 수
def drawProb(n):
    return pow(3,n) - 3*(pow(2,n)-2)



N, K = map(int, sys.stdin.readline().strip().split())

prob = [[0] * 3 for i in range(N)]

for i in range(N):
    prob[i] = list(map(float, sys.stdin.readline().strip().split()))

for i in range(N):
    print(prob[i])

