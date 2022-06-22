# n th fibonacci number
def fibo(n):
    if n<=0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter n : "))
print(fibo(n))