l=[1,2,3,4,5,6,7]
se=3
si=0
li=len(l)-1
while(si<=li):
    mid=(si+li)//2
    if l[mid]==se:
        print("found")
        break
    elif se>l[mid]:
        si=mid+1
    
    else:
        li=mid-1
else:
    print("not")  