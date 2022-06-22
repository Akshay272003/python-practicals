# max of 2
def maximum(a,b):
    if(a > b):
        return a 
    elif(a == b):
        return "Equal"
    else :
        return b

a = int(input("Enter a : "))
b = int(input("Enter b : "))
print(maximum(a,b))
