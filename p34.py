# check armstrong
n = int(input("Enter a number: "))
n = str(n)
l = len(n)

sum = 0
for i in n:
    sum += int(i)**l
if(sum == int(n)):
    print("Armstrong")
else:
    print("Not Armstrong")

