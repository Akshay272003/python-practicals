# perfect numbers
n = int(input("Enter a number : "))
sum = 0
for i in range(1, n//2+1):
    if(n%i == 0):
        sum += i
if(n == sum):
    print("Perfect Number")
else:
    print("ImPerfect")