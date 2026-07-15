"""SAFE"""
Pass = input()
code = input()
if Pass == "H" and code == "4567":
    print("safe unlocked")
elif Pass == "H" and code != "4567":
    print("safe locked - change digit")
elif Pass != "H" and code == "4567":
    print("safe locked - change char")
elif Pass != "H" and code != "4567":
    print("safe locked")
