"""coke"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if not d:
    TOTAL = 0
elif not b:
    TOTAL = d * a
else:
    P = (d-1)// b
    TOTAL = a*(d-P)+(c*P)


print(TOTAL)
