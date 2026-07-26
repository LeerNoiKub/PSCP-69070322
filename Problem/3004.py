"""Sratch"""
import math as H
X1 ,Y1 ,Z1 = map(int, input().split())
X2 ,Y2 ,Z2 = map(int, input().split())
d = H.sqrt(((X1 - X2)**2) + ((Y1 - Y2)**2) + ((Z1 - Z2)**2))
print(f"{d:.2f}")
