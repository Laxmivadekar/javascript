n=int(input('enter the number: '))
l=[]
for i in range(0,n):
    user_input=int(input('enter the number: '))
    l.append(user_input)
print(l)
c_e=0
c_o=0
for i in l:
    if i%2==0:
        c_e+=1
    else:
        c_o+=1
if c_e>c_o:
    print("READY FOR BATTLE")
else:
    print('NOT READY FOR BATTLE')
