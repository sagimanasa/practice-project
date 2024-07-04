print("while")
x=0
while (x<3):
    x=x+1
    print("hii")
print("while with if,else")
x=0
while(x<5):
    x=x+1
    print("hello")
else:
    print("hi")
# print("while with infinite loop")
# x=0
# while(x==0):
#     print("M")
print("list")
x=["hi","hello","M","H"]
for item in x:
    print(item)
print("tuple")
a=("hii","hello","M","H")
for item in a:
    print(item)
print("string")
x='This is Manasa'
for i in x:
    print(i)
    #break
print("dictionary")
x={'a':5,'b':4,'c':3}
for i in x:
    print(i,x[i])
for letter in "manasa":
    if letter=='e'or letter=='a':
        print(letter)
    else:
        print(None)
        #break