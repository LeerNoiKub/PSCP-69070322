"""Temp"""
num = float(input())
temp1 = input()
temp2 = input()
if temp1 == "C":
    if temp2 == "K":
        total = num + 273.15
        print(f"{total:.2f}")
    elif temp2 == "R":
        total = (num + 273.15) * 9 / 5
        print(f"{total:.2f}")
    elif temp2 == "F":
        total = num * 9 / 5 + 32
        print(f"{total:.2f}")
    else :
        print(num)
elif temp1 == "F":
    if temp2 == "C":
        total = (num - 32 ) * 5 / 9
        print(f"{total:.2f}")
    elif temp2 == "R":
        total = num + 459.67
        print(f"{total:.2f}")
    elif temp2 == "K":
        total = (num - 32) * 5 / 9 + 273.15
        print(f"{total:.2f}")
    else :
        print(num)
elif temp1 == "R":
    if temp2 == "C":
        total = (num - 491.67) * 5/9
        print(f"{total:.2f}")
    elif temp2 == "K":
        total = num * 5/9
        print(f"{total:.2f}")
    elif temp2 == "F":
        total = num - 459.67
        print(f"{total:.2f}")
    else :
        print(num)
elif temp1 == "K":
    if temp2 == "C":
        total = num - 273.15
        print(f"{total:.2f}")
    elif temp2 == "R":
        total = num * 1.8
        print(f"{total:.2f}")
    elif temp2 == "F":
        total = (num - 273.15) * 9 / 5 + 32
        print(f"{total:.2f}")
    else :
        print(num)
