x = int(input("Enter t : "))

for i in range(x):
    n = int(input("Enter n : "))
    print("Enter List ")
    d = {}
    l = []
    for k in  range((n*2)+2):
        p = int(input())
        if p in d.keys():
            d[p] += 1
        else:
            d[p] = 1
    for j in d.keys():
        if(d[j] == 1):
            l.append(j)
    l.sort()
    print(l)