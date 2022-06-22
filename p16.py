# traffic signal status
color = input("Enter the current color : ")
if color == "red":
    print("Stop!")
elif color == "yellow":
    print("Wait.")
elif color == "green":
    print("Keep Going")
else:
    print("Invalid Input")