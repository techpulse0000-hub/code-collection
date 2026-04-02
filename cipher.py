print('this program will encrypt your message in ceaser cipher')
A = []
encode = input('pls type in a message to be encode: ')
L = list(encode)
for code in L:
    if code.isupper():
        code = code.lower()

    
    if code == 'a':
        code = 'd'
    elif code == 'b':
        code = 'e'
    elif code == 'c':
        code = 'f'
    elif code == 'd':
        code = 'g'
    elif code == 'e':
        code = 'h'
    elif code == 'f':
        code = 'i'
    elif code == 'g':
        code = 'j'
    elif code == 'h':
        code = 'k'
    elif code == 'i':
        code = 'l'
    elif code == 'j':
        code = 'm'
    elif code == 'k':
        code = 'n'
    elif code == 'l':
        code = 'o'
    elif code == 'm':
        code = 'p'
    elif code == 'n':
        code = 'q'
    elif code == 'o':
        code = 'r'
    elif code == 'p':
        code = 's'
    elif code == 'q':
        code = 't'
    elif code == 'r':
        code = 'u'
    elif code == 's':
        code = 'v'
    elif code == 't':
        code = 'w'
    elif code == 'u':
        code = 'x'
    elif code == 'v':
        code = 'y'
    elif code == 'w':
        code = 'z'
    elif code == 'x':
        code = 'a'
    elif code == 'y':
        code = 'b'
    elif code == 'z':
        code = 'c'
    
    
    A.append(code)

print(A)
print('this is your cipher: ', ''.join(A))


    
    
      
