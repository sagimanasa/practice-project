def digit_word(num):
    digit_words={
        '0':'zero',
        '1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine'
    }
    num_str=str(num)
    # result=(digit_words(digit))
    for digit in range(num_str):
        result = (digit_words(digit))
    return''.join(result)
num=9
x=digit_word(num)
print(x)



