    
def function1(arr , n):
    for i in range(0 ,n):
        if (arr[i] != -1 and arr[i] != i):
            p = arr[i]
            while arr[p] != -1 and arr[p] != p:
                y = arr[p]
                arr[p] = p
                p = y
            arr[p] = p;
            if(arr[i] != i):
                arr[i] = -1
    return arr

ar = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8,11, 10, 9, 5, 13, 16, 2, 14, 17, 4]     
le = len(ar)
ary = function1(ar , le)
print(ary)
