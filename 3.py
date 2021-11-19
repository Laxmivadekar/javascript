'''integers = [1, 16, 3, 39, 26, 4, 8, 16, 39]

unique_integers = set(integers)  # set([1, 3, 4, 39, 8, 16, 26])

largest_integer = max(unique_integers)  # 39
print(largest_integer)
unique_integers.remove(largest_integer)

second_largest_integer = max(unique_integers)  # 26
print(second_largest_integer)'''


user = int(input())
count = 2
while(count<user):
    count = count + 1
    if count % 5 == 0:
        print ("wow!! lots of chocolates")
        count = count + 1
        break
    if count % 3 == 0:
        print ("choco")
    if count % 7 == 0:
        print ("late")
    if count % 11 == 0:
        print ("chocolate")
    else:
        print("not here")
    count = count + 3
count = count + 1
print (count)