"""JODARAIWA"""
import math as B 
a = float(input())
b = float(input())
c = float(input())
s = (a+b+c)/2
area = B.sqrt((s * (s-a) * (s-b) * (s-c)))
print(f"{area:.3f}")
