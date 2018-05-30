def modRearr(arr , n):
    arr.sort()
    temp = [0] * (n+1)
    i=0
    j=n-1
    index = 0
    
    while(i <= n // 2 or j > n // 2):
        temp[index] = arr[i]
        index += 1
        temp[index] = arr[j]
        index += 1
        i += 1
        j -= 1
    for p in range(0,n):
        arr[p] = temp[p]
    return arr
a = [5, 8, 1, 4, 2, 9 , 3, 7, 6]
ln = len(a)

ar = modRearr(a,ln)

print(ar)
