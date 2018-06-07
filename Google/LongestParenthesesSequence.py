x = int(input("Enter t : "))

for i in range(x):
    s = input("Enter Parentheses Sequence : ")
    d = {}
    for k in s:
        if (k in d.keys()):
            d[k] += 1
        else:
            d[k] = 1 
    l = []
    for p in d.keys():
        l.append(d[p])
    
    z = min(l)

    print(2*z)