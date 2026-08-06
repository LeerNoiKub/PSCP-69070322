"""AB"""
a = int(input())
b = int(input())
d = int(input())
r = int(input())
num = 0
for i in range(a,b + 1):
    if i % d == r :
        num += 1

print(num)
