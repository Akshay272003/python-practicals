# grade distributing
total_marks = int(input("Enter total marks in 5 subjects : "))
avg = total_marks/5
print("Percantage : ", avg)
if avg > 90:
    print("A+")
elif avg <= 90 and avg > 80:
    print("A")
elif avg <= 80 and avg > 70:
    print("B")
elif avg <= 70 and avg > 60:
    print("C")
elif avg <= 60 and avg > 50:
    print("D")
elif avg <= 50 and avg > 40:
    print("E")
else:
    print("Fail")