def createList():
    l=[ ]
    for i in range (5):
        s=int(input("Enter String:"))
        l.append(s)

def strlen(l):
    count=0
    for i in l:
        for j in i:
            if(l%2==0):
                count+=1
        return(count)

createList()
ans=strlen(l)
print(ans)
