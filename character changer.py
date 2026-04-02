#---mon, 8th/aug./2024---
""" p is the name of the paragraph """
c = input("which word are you replacing? ")
d = input("what are you replacing it with? ")
def replacement(a, b):
    e = p.replace(a, b).join([' ', ' '])
    return e

m = replacement(c, d)
print(m)

##new program
""" upper case changer """
def cap(a):
    l = list(a)
    for i in range(len(l)):
        if l[i] == 'i ':
            l[i] = 'I'
        elif l[i] == '.':
            l[i+2] = l[i+2].upper()
        elif l[i] == '!':
            l[i+2] = l[i+2].upper()
        elif l[i] == '?':
            l[i+2] = l[i+2].upper()
        else:
            continue
    print(''.join(l))

cap('where? i am coming now')


    

