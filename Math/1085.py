#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1085

x,y,w,h = map(int, input().split())

minResult = min(w-x,h-y,x,y)

print(minResult)