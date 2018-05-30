def modDouble(arr , n):
    count = 0
    for i in range(0,n):
        if(arr[i] != 0):
            arr[count] = arr[i]
            count += 1
    while count<n :
        arr[count] = 0
        count += 1
    if n == 1:
        return arr
    for i in range(0,n-2):
        if (arr[i] != 0) and (arr[i] == arr[i+1]):
            arr[i] = arr[i]*2
            arr[i+1] = 0
            i += 1
    count = 0
    for i in range(0,n):
        if(arr[i] != 0):
            arr[count] = arr[i]
            count += 1
    while count<n :
        arr[count] = 0
        count += 1
    return arr
a = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
ln = len(a)
ar = modDouble(a,ln)
print(ar)


