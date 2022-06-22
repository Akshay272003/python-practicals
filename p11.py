# element insertion in sorted list
# import bisect
# def insert(lis, n):
#     bisect.insort(lis, n)
#     return lis

# lis = [1,2,4]
# n = 3
# print(insert(lis, n))

def insert(lis, n):
    lis.append(n)
    lis.sort()
    return lis

lis = [1,2,4]
n = 3
print(insert(lis, n))