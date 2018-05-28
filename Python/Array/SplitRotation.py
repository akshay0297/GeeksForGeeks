def splitRotate(arr , n , key):
    temp = []
    for i in range(0,key):
        temp.append(arr[i])
    for j in range(key , n):
        arr[j-key] = arr[j]
    for k in range(n-key , n):
        arr[k] = temp[k-n+key]
    return arr
a = [1,2,3,4,5]
le = len(a)
k = int(input("Enter split Point : "))
ar = splitRotate(a,le,k)
print(ar)
