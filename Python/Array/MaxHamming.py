def maxHamming(arr , n):
    d = {}
    for i in range(n):
        if arr[i] in d.keys():
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    print(d)
    max = 0
    for j in d.keys():
        if d[j] > max :
            max = d[j]
    if max > n//2:
        p = max - (n//2)
    else:
        p = 0
    if d[j] != n :
        res = n-p
    else:
        res = 0
    return res
a = [1,2,2,2,3]
ln = len(a)
x = maxHamming(a,ln)
print(x)
