def lower_case(sentence):#converts uppercases into lowercas
    return ' '.join([word.lower()for word in str.split(sentence)])
sentence="My Name Is Manasa"
print(lower_case(sentence))

def swap_case(sentence):#inverse opertaion
    return ' '.join([word.swapcase()for word in str.split(sentence)])
sentence="My Name Is Manasa"
print(swap_case(sentence))

def upper_case(sentence):#converts all lowercase into uppercase
    return ' '.join([word.upper()for word in str.split(sentence)])
sentence="My Name Is Manasa"
print(upper_case(sentence))

def translate_case(sentence):#
    return ' '.join([word.translate(sentence)for word in str.split(sentence)])
sentence="my Name is Manasa"
print(translate_case(sentence))

def title_case(sentence):#converts first letter of words in string as capital
    return ' '.join([word.title()for word in str.split(sentence)])
sentence="My Name Is Manasa"
print(title_case(sentence))

x="MY NAME IS MANASA"
y=x.isupper()
print(y)

x="MY NAME IS MANASA"
y=x.islower()
print(y)

x="my name is manasa"
y=x.islower()
print(y)

x="my name is manasa"
y=x.endswith(".")
print(y)

x="my name is manåsa"
y=x.encode()
print(y)

x="my name is manasa"
y=x.capitalize()
print(y)

def camel_case(sentence):
    return (sentence.title())
sentence="my name is manasa"
print(camel_case(sentence))
