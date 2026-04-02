universe = 'hi442nm233ag2'
N = ['d' if i == '4' else 'e' if i == '2' else 's' if i == '3' else i for i in universe  ]
N.insert(6, ' ')
N = ''.join(N)
print(N)


b = 21
f = [ "even" if i%2 == 0 else "odd" if i%2 == 1 else i for i in range(b)]
print(f)