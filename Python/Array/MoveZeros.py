def moveZeros(arr,n):
    start  = 0
    stop = n-1
    while start < stop:
        if arr[start] == 0 and arr[stop] !=0 :
            arr[start] , arr[stop] = arr[stop] , arr[start]
        if arr[start] != 0:
            start += 1
        if arr[stop] == 0:
            stop -= 1
    return arr

a = [1, 2, 0, 4, 3, 0, 5, 0]
ln = len(a)

ar = moveZeros(a,ln)
print(ar)

