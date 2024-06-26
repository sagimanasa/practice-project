#Arithmetic operators
# addition(+)
a=10
b=3
print(a+b)
a=10
b=3.45
print(a+b)
a=10+5j
b=20.5
print(a+b)
#subtraction(-)
a=10
b=3
print(a-b)
a=10
b=3.45
print(a-b)
a=10+5j
b=20.5
print(a-b)
#multiplication(*)
a=10
b=3
print(a*b)
#division(/)
a=10
b=3
print(a/b)
print(b/a)
#modulus(%)
a=5
b=3
print(a%b)
print(b%a)
#exponent(**)
a=9
b=2
print(a**b)
print(b**a)
#floor division(//)
a=9
b=-2
print(a//b)
#comparision operators(<,>,<=,>=,==,!=)(this will show either true or false as result)
a=6
b=3
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)
#Assignment operators(+=,-=,*=,%=,**=,//=)
a=10
b=11
a+=b #a=a+b
print(a)
a-=b
print(a)
a*=b
print(a)
a%=b
print(a)
a**=b
print(a)
#logical operators(and,or,
a=[10,20,30]
b=[4,5]
c=[2]
print(a and b)
print(a or b)
a=True
print(not a)
x=3
print(not(x>2 and x<3))
#bitwise operator(&,|,^,~,<<,>>)
a=3
b=2
print(a&b) #logical and (if both a and b are 1 output is 1)
print(a|b) #logical or (if either a or b is 1 or both are 1 output is 1)
print(a^b) # xor (if either a or b is 1 output is 1)
print(~b) # not (reverse of input )
print(a<<2) #left shift
print(a>>2) #right shift
#membership operators(in,notin)
x="manasa"
a="m"
b="y"
c="a"
print(a in x)
print(b not in x)
print(c not in x)
print(b in x)
var={1:2,3:5,2:6}
a=5
b=2
print(a in var)
print(a not in var)
var=[20,30,40,50]
a=20
b=50
c=a-b
print(a in var)
print(b not in var)
print(c in var)
print(c not in var)

#identity operators(is,is not)
a=[2,3,4,5]
b=[2,3,4,5]
b=c
print(b is not a)
print(b is c)
print(b is not c)
#string operators
#concatinate
a="hello"
b=5.0
print(a+str(b))
a1="hello"
b2="world"
print(a1+b2)
#repeat(*)
a="hii"
print(a*2)
#escape(\)
#a="hello"world!"" # it throws error because interpretor will get confused if double qoutes are placed in between strings
a="hello\"world!\""
print(a)
a='hello"world"'
print(a)
a='hello"world!"'
print(a)
a=4+5/6*3
print(a)
a=4+5/3
print(a)
var=[20,30,40,50]
a=20
b=50
c=a-b
print(a in var)
print(b not in var)
print(c in var)
print(c not in var)
var=(10,20,30,40)
a=10
b=20
print((a,b) in var)
var=((10,20),30,40)
a=10
b=20
print((a,b) in var)
a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=a
print(a is b)
print(b is not  c)
print(a is c)
print(a is not c )