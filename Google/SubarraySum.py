x = int(input("Enter t : "))

for i in range(x):
    n ,sum = int(input("Enter N :")) ,int(input("Enter S :"))
    l = []
    print("Enter List : ")
    for j in range(n):
        z = int(input())
        l.append(z)
    l.sort()
    flag = 0
    left = 0 
    right = n-1
    while left < right :
        if l[left] + l[right] == sum :
            flag =1
            break
        elif l[left] + l[right] < sum:
            left += 1
        else:
            right -= 1
    if flag == 0:
        print("NO")
    else:
        print("Yes")

