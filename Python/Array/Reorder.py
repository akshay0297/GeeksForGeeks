def reorder(arr , ind , n):
    temp = [0]*n
    for i in range(0 , n):
        temp[ind[i]] = arr[i]
    return temp
a =  [10, 11, 12]
r = [1, 0, 2]
ln = len(a)

ar = reorder(a,r,ln)

print(ar)
