#  My position is 1st and my friend come on 4th
# output : 5
# a='My position is 1st and my friend come on 4th 9556'
# a=input('enter the sentance: ')
# sum=0
# for i in a:
#     b=i.isdigit()
#     if b==True:
#         c=int(i)
#         sum+=c
#     else:
#         pass
# print(sum)


# a=[1,2,'5',4,'99',49,'15']
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==int:
#         sum+=a[i]
#     else:
#         integer=int(a[i])
#         sum+=integer
#     i+=1
# print(sum)

# dict1={1:"shailaja",2:"sarika"}
# a=[]
# a.append(dict1)
# dict1[3]='Lucky'
# a.append(dict1)
# print(a)


# l=[]
# i=1
# while i<=12:
#     l.append([i])
#     i+=1
# print(l)

# sum=0
# def f(a):
#     def inner():
#         sum=10+15
#         return sum
#     b=print(inner())
# f(sum)

# def n(a):
#     if a==0:
#         return a

#     return n(a-2)
# print(n(20))
# arr=[]
# arr.append(list(map(int, input('enter the number: ').strip().split())))[:2]
# print(arr)
'''n=int(input("enter the num"))
a=list(map(int, input('enter the number: ').strip().split()))[:n]
print(a)'''
# Python program to execute
# main directly
'''print ("Always executed")

if __name__ == "__main__":
	print ("Executed when invoked directly")
else:
	print ("Executed when imported")'''

# print(0.1+0.1+0.1==0.3)
a=0.1+0.1+0.1
b=0.3
print(a)
print(b)
print(a==b)