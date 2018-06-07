x = int(input("Enter t : "))

for i in range(x):
    n = int(input("Enter n : "))
    print("Enter List ")
    l = []
    for k in  range(n):
        p = int(input())
        l.append(p)
    kmj = []
    

    for j in range(0,n-1):
        test = []
        for k in range(j+1 , n):
            if l[j] <= l[k]:
                kmj.append(k-j)
            else:
                break
    print(kmj)
    print("Max Gap  = " , max(kmj))