"""ROIHO"""
Pro = int(input())
Y = int(input())
M = int(input())
ACTP = int(input())
if ACTP > Pro and Pro == "4":
    total = ((M*ACTP) - ((ACTP//Pro)*M))
    print(total)
elif ACTP < Pro :
    total = M*ACTP
    print(total)
