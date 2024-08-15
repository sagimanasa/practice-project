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


def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+1
    if sum==n:
        return True
    return False
n=12
print(perfect_number(n))





