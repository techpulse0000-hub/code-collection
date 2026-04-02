original = input('what is the name of the file: ')

with open(original, 'r') as f:
    a = []
    for i in f:
        a.append(i)
        
        

b = []    
for j in a:
    v = j
    v = v.lower()
    for k in range(len(v)):
        if v[k] == '#':
            b.append(v[:k])
            break
        else:
            b.append(v)
            break

print(''.join(b))