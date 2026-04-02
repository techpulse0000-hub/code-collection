D = ['sunday', 'monday', 'teusday', 'wednesday', 'thursday', 'friday', 'saturday']
W = ['sunny', 'rainy']
C = [['chelsea', 'man city', 'barca', 'R-madrid', 'bayer-M', 'green T-shirt', 'blue shirt'], ['black trouser', 'brown trouser', 'blue jean', 'ash pants', 'blue trouser', 'black jean', 'blue jean']]
A = ['jacket', 'rain coat', 'umbrella', 'hand glove', 'hoodie', 'face cap']

Q2 = input('what is the condition of the weather ')

if Q2 == W[0]:
    print('pick up a shirt and a trouser from the closet and you dont need to put on an accessory')
elif Q2 == W[1]:
    print('pick up a shirt and a trouser from the closet and you have to put on an accessory', '\n', 'dont forget your ', A[0], ', ', A[1], 'and your ', A[2])
else:
    print('input a valid weather condition  ')

