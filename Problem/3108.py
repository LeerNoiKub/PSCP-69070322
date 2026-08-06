"""promo"""
a ,b ,c = map(int, input().split())
pen = a * 25
book = b * 40
color = c * 55
total = pen + book + color
if a + b + c >= 3:
    total = total * 90 // 100
    print(f"{total:.0f}")
else:
    print(total)
