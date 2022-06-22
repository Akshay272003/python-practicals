# prime number
n = int(input("Enter a number : "))
flag = True
if n>0:
    for i in range(2, n//2+1):
        if(n%i == 0):
            flag = False
            break
else:
    flag = False
if flag==True:
    print("Prime number")
else:
    print("Not prime")