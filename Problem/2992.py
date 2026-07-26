"""FYM"""
num1 = input()
num2 = num1[::-1]
num3 = int(num1)
num4 = int(num2)
All = 0
mark = input()
if mark == "+" :
    All = num3 + num4
elif mark == "*" :
    All = num3 * num4
print(f"{num3} {mark} {num4} = {All}")
