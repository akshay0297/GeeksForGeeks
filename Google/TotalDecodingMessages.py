t = int(input())

for i in range(t):
    n = int (input())
    s = input()
    if '0' in s:
        count = 0
    else:
        count = 1
    flag = 1
    l = []
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
        print("St : " , count)
        for k in range(0 , n-1):
            if s[k] == '1' or s[k] == '2' and s[k+1] <'7':
                count += 1
                print("H : " , count)
                st = ""
                if k == 0:
                    st = s[k+2:n]
                else:
                    st = s[0:k]+s[k+2:n]
                print("STR = " , st)
                m = len(st)
                print ("Ctr  = " , count)
                for d in range(m-1):
                    if st[d] == '1' or st[d] == '2' and st[d+1] <'7':
                        l.append(st[d:d+2])
                        count += 1 
                    print(st[d] , st[d+1] , "Inside : " , count)
                #count -= 1
            print(s[k] , s[k+1] , "Outside: " , count)
        print ("Final : " , count)
#few test cases not working
