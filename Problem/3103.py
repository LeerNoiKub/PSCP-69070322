"""pool"""
num = int(input())
sara = ["a", "e", "i", "o", "u"]
six7 = 0
for i in range(num) :
    letter = input().lower()
    if letter in sara:
        six7 = six7 + 1 + i - i
print(six7)
