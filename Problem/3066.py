"""same"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 == num2 == num3:
    print("all the same")
elif num1 == num2 or num2 == num3 or num3 == num1:
    print("neither")
else:
    print("all different")
