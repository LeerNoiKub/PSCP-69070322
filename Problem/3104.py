"""ticket cal"""
age_day = input().split()
agee = age_day[0]
age = int(agee)
day = age_day[1]
tikcet_s = 100
tikcet_a = 150
if age < 5:
    print(0)
elif 5 <= age <= 18:
    if day == "Wed":
        tikcet_s = tikcet_s // 2
        print(tikcet_s)
    else:
        print(100)
elif age >= 19:
    if day == "Wed":
        tikcet_a = tikcet_a // 2
        print(tikcet_a)
    else:
        print(150)
