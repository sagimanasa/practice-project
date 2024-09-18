##even or odd
# def is_number(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# num=5
# print(is_number(num))
##ouput:odd

# #prime or not
# def is_prime(num):
#     if num<2: #it returns false because prime numbers are greater than 2
#         return False
#     for i in range(2,num):
#         if num%i==0: #it checks number is divisible or not becuase prime number divisible by itself only
#             return False
#     return True
# num=4
# if is_prime(num):
#     print("prime number")
# else:
#     print("not prime number")
#
# #output:not prime number

# #swapping two number
# def swap(num1,num2):
#     temp=num1
#     num1=num2
#     num2=temp
#     print(num1)
#     print(num2)
# num1=3
# num2=2
# swap(num1,num2)
# #output:2
# #       3

# #generate fibonocci series
# def fibonocci(n):
#     if n==0:
#         return []
#     if n==1:
#         return [0]
#     if n==2:
#         return[0,1]
#     output=[0,1]
#     for i in range(2,n):
#         output.append(output[i-1]+output[i-2])
#     return output
# print(fibonocci(5))
# #output:[0,1,1,2,3]


