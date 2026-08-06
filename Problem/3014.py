"""milk"""
bottle = int(input())
head = int(input())
head1 = int(input())
money = int(input())
buy = money // bottle
if head > 0:
    if head1 >= 0 and head1 < head:
        gain = buy // head
        gain1 = gain * head1
        total = buy + gain1
        print(total)
    else:
        print(buy)
elif head <= 0:
    print(buy)
else:
    print(buy)
