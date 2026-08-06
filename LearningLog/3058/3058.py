"""brick"""
a = int(input())
b = int(input())
goal = int(input())
b1 = b * 5
goal1 = goal % 5
total = a + b1
if b1 >= goal and total != goal and a >= goal1:
    print(goal1)
elif total >= goal and (goal - b1) > 0:
    print(goal-b1)
elif total == goal:
    print(a)
elif b1 >= goal and not goal1:
    print(0)
else:
    print(-1)
