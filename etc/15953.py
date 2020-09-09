# 가정한 횟수
T = int(input())
# fest1 상금
fest1 = [0, 500, 300, 300, 200, 200, 200, 50, 50, 50, 50, 30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]
# fest2 상금
fest2 = [0, 512, 256, 256, 128, 128, 128, 128, 64, 64, 64, 64, 64, 64, 64, 64, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]
answer = []
# 가정에 대한 정보 [a,b]
for _ in range(T):
    a, b = map(int, input().split())
    if a > 21:
        if b >= 0 and b <= 31:
            answer.append(fest2[b]*10000)
        else:
            answer.append(0)
    else:
        if b >= 0 and b <= 31:
            answer.append((fest1[a]+fest2[b])*10000)
        else:
            answer.append(fest1[a]*10000)
for ans in answer:
    print(ans)