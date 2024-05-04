s1=input()
s2=input()
for i in s1:
    if i in s2:
        s1=s1.replace(i,'',1)
        s2=s2.replace(i,'',1)
print(s1)
print(s2)
z=len(s1)+len(s2)
print(z)
f="flames"
while len(f)>1:
    q=z%len(f)-1
    if q>=0:
        x=f[q+1:]
        y=f[:q]
        f=x+y
    else:
        f=f[:len(f)-1]
print(f[0])



 
               
               