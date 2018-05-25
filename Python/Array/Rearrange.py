def rearrange(arr , n):
    j = -1
    for i in range(n):
        if arr[i]<0 :
            j += 1
            arr[i] , arr[j] = arr[j] , arr[i]
    x = j+1
    y = 0

    while (x<n and y<x and arr[y]<0):
        arr[x] , arr[y] = arr[y] , arr[x]
        x += 1
        y += 2
    return arr

ar = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
le = len(ar)
arrr = rearrange(ar,le)

print(arrr)
