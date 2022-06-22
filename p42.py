# print prime in range

def is_prime(p):
    for i in range(2,p//2+1):
        if(p%i == 0):
            return 0
    return 1

a = int(input("Enter the start : "))
b = int(input("Enter the end : "))
for i in range(a,b+1):
    if is_prime(i):
        print(i, end=" ")
    