# print first n prime number

def is_prime(p):
    for i in range(2,p//2+1):
        if(p%i == 0):
            return 0
    return 1

n = int(input("Enter a number : "))
count = 0
for i in range(2,99999999):
    if is_prime(i):
        print(i, end=" ")
        count += 1
    
    if count == n:
        break
