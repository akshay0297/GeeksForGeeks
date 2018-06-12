class stack:
    
    def __init__(self):
        self.items = []
    
    def empty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def push(self , data):
        self.items.append(data)
    
    def pop(self):
        if self.empty() == True:
            return
        return self.items.pop()
    
t = int(input("Enter T : "))

for i in range(t):
    s = stack()
    s.push(-1)
    seq = input("Enter Parentheses Sequence : ")
    count = 0
    opc = 0
    clc = 0
    for k in range(len(seq)):
        if seq[k] == '(':
            s.push(k)
            opc += 1
        else:
            clc += 1
            s.pop()
            if s.empty() == False:
                count = max(count , k - s.items[len(s.items) - 1])
            else:
                s.push(k)
    print(count)