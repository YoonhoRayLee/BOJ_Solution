#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1924

thirtyOne = [1,3,5,7,8,10,12]
thirty = [4,6,9,11]
twentyEight = [2]
weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int, input().split())
sumDays = 30
if x == 1:
    print(weekday[(y-1)%7])
else:
    for i in range(2, x+1):
        if i == x:
            break
        else:
            if i in thirtyOne:
                sumDays += 31
            elif i in thirty:
                sumDays += 30
            elif i in twentyEight:
                sumDays += 28
    sumDays += y
    print(weekday[sumDays%7])