#palindrome
n = input("Enter a number: ")
temp = n[::-1]
if n == temp:
    print("Palindrome")
else:
    print("Not Palindrome")