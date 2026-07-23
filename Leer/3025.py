"""month"""
m = int(input())
d = int(input())
if m <= 3:
    if m == 3 and d >= 21:
        print("spring")
    else :
        print("winter")
elif m <= 6:
    if m == 6 and d >= 21:
        print("summer")
    else:
        print("spring")
elif m <= 9:
    if m == 9 and d >= 21:
        print("fall")
    else:
        print("summer")
elif m <= 12:
    if  m == 12 and d >= 21:
        print("winter")
    else:
        print("fall")
