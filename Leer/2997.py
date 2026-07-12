"""JEL"""
Ra = int(input())
Rb = int(input())
WORD = str(input())
if WORD == "B" :
    Turtle = 1/(1+10**((Ra- Rb) /400))
    print(f"{Turtle:.2f}")
elif WORD == "A" :
    Turtle = 1/(1+10**((Rb- Ra) /400))
    print(f"{Turtle:.2f}")
