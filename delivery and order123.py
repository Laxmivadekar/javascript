n=int(input('enter the number: '))
order=list(map(int,input('enter the order :' ).rstrip().split()))
pre=list(map(int,input('enter the order :' ).rstrip().split()))
d={}
l=[]
for i in range(0,n):
    time=order[i]+pre[i]
    d[i]=time
    l.append(time)  #{1: 9, 2: 6, 3: 11, 4: 4, 5: 7}
a_o=l
b_s=l.copy()
b_s.sort() #[4, 6, 7, 9, 11]
print(b_s)
if a_o==b_s:
    s_l=[]
    for i in d.keys():
        s_l.append(i)
    print(s_l)
else:
    l1=[]
    i=0
    while i<len(b_s):
        for j in d:
            if b_s[i]==d[j]:
                l1.append(j)
        i=i+1
    print(l1)

