"""circle"""
import math as m
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())
cross = m.sqrt((x2-x1)**2 + (y2-y1)**2)
r3 = r1 + r2
if cross >= r3 :
    print("no overlapping")
elif cross < r3 :
    print("overlapping")
