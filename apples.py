s=int(input('enter the no: '))
t=int(input('enter the no: '))
a=int(input('enter the no: '))
b=int(input('enter the no: '))
a_l=[]
b_l=[]
for i in range(1,4):
    a_d=int(input('enter the apples distance: '))
    b_d=int(input('enter the oranges distance: '))
    a_l.append(a_d)
    b_l.append(b_d)
# distance to the position of the tree, they land at
a_land=[]
b_land=[]
i=0
while i<3:
    m=a+a_l[i]
    n=b+b_l[i]
    a_land.append(m)
    b_land.append(n)
    i=i+1
a_c=0
for k in a_land:
    if  k==7 or k==8 or k==9 or k==10:
        a_c+=1
b_c=0
for l in b_land:
    if l==7 or  l==8 or  l==9 or l==10:
        b_c+=1
print(a_c)
print(b_c)

