"""Rabbit"""
W1 , L1 , F1 = map(int ,input().split())
Cost = int(input())
space = ((W1 + L1)*2) * F1
total = space * Cost
print(space)
print(total)
