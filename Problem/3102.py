"""cul car tax """
y = int(input())
motor = int(input())
if y <= 1990 :
    if motor <= 1500 :
        print(1250)
    elif 1500 < motor <= 2000 :
        print(1400)
    elif motor > 2000:
        print(2000)
if 1991 <= y <= 1999 :
    if motor <= 1500 :
        print(1100)
    elif 1500 < motor <= 2000 :
        print(1300)
    elif motor > 2000:
        print(1700)
if y >= 2000 :
    if motor <= 1500 :
        print(1000)
    elif 1500 < motor <= 2000 :
        print(1200)
    elif motor > 2000:
        print(1500)
