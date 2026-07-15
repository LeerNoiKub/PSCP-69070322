"""ROIHO"""
Pro = int(input())
Y = int(input())
M = int(input())
ACTP = int(input())
Live = (((ACTP // Pro)*Y) + (ACTP % Pro))*M
print(Live)
