n=int(input('enter the number: '))
d={}
l=[]
for i in range(1,n+1):
    order=int(input('enter the order :' ))
    pre=int(input('enter the pre: '))
    time=order+pre
    d[i]=time
    l.append(time)
print(d)  #{1: 9, 2: 6, 3: 11, 4: 4, 5: 7}
a_o=l
print(a_o)
b_s=l.copy()
b_s.sort() #[4, 6, 7, 9, 11]
print(b_s)
# temp=0
# for i in range(0, len(b_s)):    
#     for j in range(i+1, len(b_s)):    
#         if(b_s[i] >b_s[j]):    
#             temp = b_s[i];    
#             b_s[i] = b_s[j];    
#             b_s[j] = temp; 
c=b_s  
# print(c)

if a_o==c:
    s_l=[]
    for i in d.keys():
        s_l.append(i)
    print(s_l)
else:
    l1=[]
    i=0
    while i<len(c):
        for j in d:
            if c[i]==d[j]:
                l1.append(j)
        i=i+1
    print(l1)

