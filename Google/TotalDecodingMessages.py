t = int(input())

for i in range(t):
    n = int (input())
    s = input()
    if '0' in s:
        count = 0
    else:
        count = 1
    flag = 1
    if '0' in s:
        c = '0'
        l = [pos for pos, char in enumerate(s) if char == c]
        
        for k in l:
            if k == 0:
                count = 0
                flag = 0
            elif s[k-1] >"2":
                flag = 0
        if flag == 0:
            count = 0
            print (count)
        else:
            count = 1
            print(count)         
    else:
        for k in range(0 , n-1):
            if s[k:k+1] < "27":
                count += 1
                st = ""
                if k == 0:
                    st = s[k+2:n-1]
                else:
                    st = s[0:k]+s[k+2:n]
                print(st)
                m = len(st)
                print ("Ctr  = " , count)
                for d in range(m):
                    if st[d:d+1] <"27":
                        count += 1 
                print(count)
        print (count)

#one test case not working
