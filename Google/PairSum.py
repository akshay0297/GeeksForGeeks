from collections import Counter
t = int(input("Enter t :"))

for i in range(t):
    a =[]
    b =[]
    n1 = int(input("Size of Array 1 : "))
    print("Enter Array 1 ")

    for j in range(n1):
        x = int(input())
        a.append(x)
    
    n2 = int(input("Size of Array 2 : "))
    print("Enter Array 2")

    for j in range(n2):
        x = int(input())
        b.append(x)

    sm = int(input("Sum =  "))

    ac = Counter()
    bc = Counter()
    # a.sort()
    # b.sort()
    for k in a:
        ac[k] += 1
    for k in b:
        bc[k] += 1    
    
    for j in ac:
        if sm - j in bc:
            for p in range(ac[j]*bc[sm-j]):
                print(j , ", " , sm-j) 
    
    # sa = 0
    # eb = n2-1

    # while sa < n1 and eb >=0:
    #     if (a[sa] + b[eb] )== sm :
    #         print (a[sa] ,",", b[eb])
    #         sa += 1
    #         eb -= 1
    #     elif (a[sa] + b[eb]) < sm:
    #         sa += 1
    #     else:
    #          eb -= 1
