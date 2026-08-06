"""brick"""
a = int(input())
b = int(input())
goal = int(input())
b1 = b * 5
total = a + b1
if total >= goal:
    if b1 >= goal:
        print(0)
    else:
        print(a)
elif total != goal:
    print(-1)
