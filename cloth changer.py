D = ['sunday', 'monday', 'teusday', 'wednesday', 'thursday', 'friday', 'saturday']
W = ['sunny', 'rainy']
C = [['chelsea', 'man city', 'barca', 'R-madrid', 'bayer-M', 'green T-shirt', 'blue shirt'], ['black trouser', 'brown trouser', 'blue jean', 'ash pants', 'blue trouser', 'black jean', 'blue jean']]
A = ['jacket', 'rain coat', 'umbrella', 'hand glove', 'hoodie', 'face cap']

Q1 = input('what day of the week is it')
Q2 = input('what is the condition of the weather')

if Q1 == D[0]:
    if Q2 == W[0]:
        print('wear this:\n', 'top: ', C[0][0], '\n', 'trouser: ', C[1][0], '\n', 'attachment: ', A[0])
    else:
        print('wear this:\n', 'top: ', C[0][0], '\n', 'trouser: ', C[1][0], '\n', 'attachment: ', A[0], ',', A[1], ',',' and', A[2])
elif Q1 == D[1]:
    if Q2 == W[0]:
        print('wear this:\n', 'top: ', C[0][1], '\n', 'trouser: ', C[1][1])
    else:
        print('wear this:\n', 'top: ', C[0][1], '\n', 'trouser: ', C[1][1], '\n', 'attachment: ', A[0], ',', A[1], ',',' and', A[2])
elif Q1 == D[2]:
    if Q2 == W[0]:
        print('wear this:\n', 'top: ', C[0][2], '\n', 'trouser: ', C[1][2], '\n', 'attachment: ', A[0])
    else:
        print('wear this:\n', 'top: ', C[0][2], '\n', 'trouser: ', C[1][2], '\n', 'attachment: ', A[0], ',', A[1], ',',' and', A[2])
elif Q1 == D[3]:
    if Q2 == W[0]:
        print('wear this:\n', 'top: ', C[0][3], '\n', 'trouser: ', C[1][3], '\n', 'attachment: ', A[0])
    else:
        print('wear this:\n', 'top: ', C[0][3], '\n', 'trouser: ', C[1][3], '\n', 'attachment: ', A[0], ',', A[1], ',',' and', A[2])
elif Q1 == D[4]:
    if Q2 == W[0]:
        print('wear this:\n', 'top: ', C[0][4], '\n', 'trouser: ', C[1][4], '\n', 'attachment: ', A[0])
    else:
        print('wear this:\n', 'top: ', C[0][4], '\n', 'trouser: ', C[1][4], '\n', 'attachment: ', A[0], ',', A[1], ',',' and', A[2])
elif Q1 == D[5]:
    if Q2 == W[0]:
        print('wear this:\n', 'top: ', C[0][5], '\n', 'trouser: ', C[1][5], '\n', 'attachment: ', A[0])
    else:
        print('wear this:\n', 'top: ', C[0][5], '\n', 'trouser: ', C[1][5], '\n', 'attachment: ', A[0], ',', A[1], ',',' and', A[2])
elif Q1 == D[6]:
    if Q2 == W[0]:
        print('wear this:\n', 'top: ', C[0][6], '\n', 'trouser: ', C[1][6], '\n', 'attachment: ', A[0])
    else:
        print('wear this:\n', 'top: ', C[0][6], '\n', 'trouser: ', C[1][6], '\n', 'attachment: ', A[0], ',', A[1], ',',' and', A[2])
else:
    print('answer the questions validly')






        

    
    
        
    




