# def staircase(num_stairs):
#     n = num_stairs - 1
#     for stairs in range(num_stairs):
#         print (' ' * n, '#' * stairs)
#         n -= 1
#     print ('#' * num_stairs)
# staircase(4)


n=int(input("enter the number: "))
s = n - 2
for stairs in range(1, n):
    print(' ' * s, '#' * stairs)
    s -= 1
print('#' * n)