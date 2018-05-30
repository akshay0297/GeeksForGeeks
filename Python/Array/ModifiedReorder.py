def modReorder(arr , n):
    temp = [0]*n
    for i in range(0,n):
        x = arr[i]
        temp[x] = i
    return temp
a = [2, 0, 1, 4, 5, 3]
ln = len(a)

z = modReorder(a , ln)
print(z)
