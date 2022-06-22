# simple interest
def sInterest(p, r, t):
    si = p*r*t/100
    return si

p = int(input("Enter principle : "))
r = int(input("Enter Rate : "))
t = int(input("Enter Time : "))

print(sInterest(p, r, t))