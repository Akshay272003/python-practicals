# sum of a digit of a number
n = input("Enter a nuber: ")
sum = 0
for i in n:
    sum += int(i)
print(f"Sum: {sum}")