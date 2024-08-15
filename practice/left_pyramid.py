def left_pyramid(n):
    if n>0:
        print("*"*n)
        left_pyramid(n-1)
n=5
print(left_pyramid(n))


def full_pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print()
n=7
print(full_pyramid(n))


def right_pyramid(n):
        for i in range(0,n):
            for j in range(0,n-i-1):
                print(" ",end="")
            for k in range(0,i+1):
                print("*",end="")
            print()                           
n=5
print(right_pyramid(n))