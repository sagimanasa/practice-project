# def perfect_number(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum=sum+1
#     return sum
# n=13
# print(perfect_number(n))
# if perfect_number(n):
#     print("perfect number")
# else:
#     print("not perefct number")


# def perfect_number(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum=sum+1
#         if sum==n:
#             return True
#     return False
# n=2
# print(perfect_number(n))

# n=int(input("enter any number:"))
# def perfect(n):
#     sum=0
#     for i in range(1,n):
#         if(n%i==0):
#             sum=sum+i
# n=6
# if(sum==n):
#     print("perfect number")
# else:
#     print("Not perfect number")


n=12
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("perfect number")
else:
    print("Not perfect number")


