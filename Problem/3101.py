"""check water status"""
tem = int(input())
letter_tem = input().lower()
if letter_tem == "c" :
    if letter_tem == "c" and tem <= 0  :
        print("solid")
    elif letter_tem == "c" and 0 < tem < 100 :
        print("liquid")
    elif letter_tem == "c" and tem >= 100 :
        print("gas")
else:
    if letter_tem == "f" and tem <= 32 :
        print("solid")
    elif letter_tem == "f" and 32 < tem < 212 :
        print("liquid")
    elif letter_tem == "f" and tem >= 212 :
        print("gas")
