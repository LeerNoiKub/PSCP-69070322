"""Pitha"""
Three = float(input())
Hi = float(input())
F = Three - Hi
avg = (F / 2) - 1
if avg < 0:
    avg = 0
dif = Hi - avg
if dif > 2:
    print("Surprising")
if dif <= 2:
    print("Not surprising")
