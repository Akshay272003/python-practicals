# matrix transpose
lis1 = []
res = []
print("Enter mat 1 : ")
for i in range(3):
    a = list(map(int, input().split()))
    lis1.append(a)

for i in range(3):
    temp = []
    for j in range(3):
        temp.append(lis1[j][i])
    res.append(temp)
for i in res:
    print(i)