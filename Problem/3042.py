"""ten"""
num = int(input())
ist = []
for i in range(num+1):
    if not i % 10:
        ist.append(i)
print(*ist[::-1])
