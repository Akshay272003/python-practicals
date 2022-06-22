# roots of quadratic eqn
from math import sqrt
a, b, c = map(int, input("Enter coefficient of a, b and c: ").split())
d = b*b - 4*a*c
x=0
y=0
if(d == 0):
    print(f"x: {-b/(2*a)}\ny: {-b/(2*a)} ")
elif(d>0):
    print(f"x: {(-b + sqrt(d))/(2*a)}\ny: {(-b - sqrt(d))/(2*a)}")
else:
    print("Imaginary roots")