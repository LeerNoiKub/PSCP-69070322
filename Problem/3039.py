"""MIN4"""
num = int(input())
mon = 1000000
for i in range(num):
    i += 1 - 1
    num1 = int(input())
    if num1 < mon:
        mon = num1

print(mon)
