# numeric datatypes
a = 123
print(type(a))  # int
b = 20.13
print(type(b))  # float
c = True
print(type(c))  # boolean
d = 10 + 3j
print(type(d))  # complex
# string datatypes
e = "hi this is manasa"
print(type(e))  # str
print(e[0])  # h
print(e[1:7])  # i this
print(e[9])  # s
print(e * 2)  # hi this is manasahi  this is manasa
print(e+"!")  # hi this is manasa!
# list datatype
f = ['abcd', 786, 2.23, 'manu', 70.2]
print(type(f))  # list
print(f[0])  # abcd
print(f[1:3])  # [786,2.23]
print(f[2:])  # [2.23,'manu',70.2]
# tuple datatype
g = ('abcd', 786, 2.23, 'manu', 70.2)
print(type(g))  # tuple
print(g[0])  # abcd
print(g[1:3])  # (786,2.23)
print(g[2:])  # (2.23,'manu',70.2)
# range datatype
for i in range(1, 5, 3):  # 1 4
    print(i)
for i in range(2, 5):  # 2,3,4
    print(i)
# bytes datatype
h = bytes([65, 66, 67, 68, 69])
print(type(h))  # bytes
print(h)  # b'ABCDE'
# bytearray datatype
i = bytearray([72, 101, 108, 108, 111])
print(type(i))  # bytearray
print(i)  # b'Hello'
