d = str(input())
def rev(x):
    r = 0
    while x > 0:
        r=r*10+x%10
        x/=10
    return r

def length(x):
    r = 0
    x = int(x)
    while True:
        r+=1
        x/=10
        if x == 0:
            return r

for p in range(200000):
    rp = rev(p)
    q = rp + int(d)
    leng = length(p)
    for t in range(2*leng-1, 2*leng+1):
        qs = ''+str(q)
        while len(qs) > t - leng:
            qs = qs[1]
        while len(qs) < t - leng:
            qs = '0'+qs
        y = p + int(qs)
        if y-rev(y) == d:
            print(''+y)
print(-1)
