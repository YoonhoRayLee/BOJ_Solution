#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.9251
import sys
str1 = sys.stdin.readline()
str2 = sys.stdin.readline()

def lcs(a,b):
    prev = [0]*len(a)
    for i, r in enumerate(a):
        current = []
        for j, c in enumerate(b):
            if r==c:
                e = prev[j-1] + 1 if i*j>0 else 1
            else:
                e = max(prev[j] if i >0 else 0, current[-1] if j> 0 else 0)
            current.append(e)
        prev = current
    return current[-1]

print(lcs(str1,str2)-1)