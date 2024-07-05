# sentence="my name is manasa"
# x=sentence.split()
# print(x)

def camel_case(sentence):
    word_list = sentence.split() #splitting the sentence as array
    print(word_list)
    # array=[]
    # for word in word_list:
    #     print(word)
    #     x= word.capitalize()
    #     array.append(x)
    for index in range(0,len(word_list)): #iteration in the range od array as word_list
        x=word_list[index]
        print(x)
        word_list[index]=x.capitalize() #converting the array value into capitalize method
    string = " ".join(word_list) #joing the updated array values as string
    print(string)
    #return ' '.join([word.title() for word in str.split(sentence)]) #title method in string converts starting letter of word as capital
    return string
sentence = "my name is manasa"
print(camel_case(sentence))
