def full_pyramid(n):
    for i in range(1,n+1):
        # print(i)
        for j in range(n-i):
            # print(j)
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print()
n=7
print(full_pyramid(n))

# Output:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************


def diagonal_star(n):
    for i in range(1,n+1):
        for j in range(1,2*i):
            print(" ",end="")
        print("*")
n=4
print(diagonal_star(n))

# Output:
# *
#    *
#      *
#        *