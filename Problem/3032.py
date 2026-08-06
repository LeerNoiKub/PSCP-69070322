"""score"""
P = int(input())
score = []
for i in range(P):
    i += 1 - 1
    score.append(int(input()))

max1 = max(score)
top = score.count(max1)
print(max1)
print(top)
