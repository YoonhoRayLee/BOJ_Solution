N = int(input())

if N < 10:
    print(N)
else:
    idx = 10
    num = 10
    while True:
        if idx == N:
            print(num)
            break
        strNum = str(num)
        revStr = ''.join(sorted(str(num))[::-1])
        if strNum == revStr:
            flag = False
            for i in range(10):
                if strNum.count(str(i)) > 1:
                    flag = True
            if not flag:
                idx +=1
        num += 1