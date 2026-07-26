"""Cal"""
n = int(input())
num = 0
count = 0
if n == 1:
    print("1")
else:
    while count < n:
        count += 1
        num += int(len(str(count))) +1
    print(num)
