t = int(input())
for i in range(t):
    n = int(input())
    s = bin(n)
    s = s[2:]
    #print(s)
    if len(s) == 8:
        pass
    else:
        while(len(s) != 8):
            s = '0'+s
    print(s)
    l = list(s)
    #print(l)
    for j in range(0 , len(l)-1 , 2):
        l[j] , l[j+1] = l[j+1] , l[j]
    #print("Swapped : " , l)
    stt =""
    for st in l:
        stt = stt + st
    
    print(stt)
    #stt = "0b" + stt
    print(int(stt , 2))