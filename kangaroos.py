
x1=int(input('enter the no: '))
v1=int(input('enter the no: '))
x2=int(input('enter the no: '))
v2=int(input('enter the no: '))
if ((x1>x2 and v1>v2) or (x1<x2 and v1<v2)):
    print("NO")
else:
  for i in range(9999):
    x1 = x1 + v1
    x2 = x2 + v2
    if x1 == x2 :
      bl = True
      break
       
  if bl == True:
    print("YES")
  else:
    print("NO")


