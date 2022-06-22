# matrix addition 3*3
lis1 = []
lis2 = []
res = []
print("Enter mat 1")
for i in range(3):
    a = list(map(int, input().split()))
    lis1.append(a)
print("Enter mat 2 : ")
for i in range(3):
    a = list(map(int, input().split()))
    lis2.append(a)

for i in range(3):
    temp = []
    for j in range(3):
        temp.append(lis1[i][j] + lis2[i][j])
    res.append(temp)

for i in res:
    print(i)
    