def indexRotation(arr ,  r , n , p , key):
    for i in range(p):
        x = arr[r[i][1]]
        for j in range(r[i][1],r[i][0],-1):
            arr[j] = arr[j-1]
        arr[r[i][0]] = x
        print(arr)
    return arr[key]
a = [1,2,3,4,5]
ranges = [[0,2],[0,3]]
ln = len(a)
lp = len(ranges)

k = int(input("Enter Index : "))

z = indexRotation(a,ranges,ln,lp,k)

print(z)
