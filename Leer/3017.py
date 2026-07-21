"""GUY"""
Cost = int(input())
service = Cost * 10 / 100
if service < 50:
    service = 50
elif service > 1000:
    service = 1000
total = Cost + service
vat = (total) * 7 / 100
bill = total + vat
print(f"{bill:.2f}")
