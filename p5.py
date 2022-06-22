# compound interest
p = int(input("Enter principle : "))
r = int(input("Enter Rate : "))
t = int(input("Enter Time : "))

amount = p*(pow((1+r/100), t))
ci = amount - p
print(ci)