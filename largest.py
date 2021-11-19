'''l_n=-1
a=[3,41,12,9,74,15]
for i in a:
    if i>l_n:
        l_n=i
    print(l_n)
print("largest no: ",l_n) 

l_n=-1
a=[3,41,12,9,74,15]
for i in a:
    if i>l_n:
        l_n=i
        print(l_n)
print("largest no: ",l_n)'''

# l_n=-1
# a=[3,41,12,9,74,15]
# i=0
# while i<len(a):
#     if a[i]>l_n:
#         l_n=a[i]
#     print(l_n)
#     i=i+1
# print("largest no: ",l_n)

# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)

'''s_n=-1
a=[3,41,12,9,74,15]
for i in a:
    if s_n<i:
        s_n=i
        print(s_n)
print("largest no: ",s_n)'''

# import urllib.request
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

'''class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()'''

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()