ages = []
admission = 0.0
age = int(input('what are their ages'))


while True:
     
     
     age = int(input('what are their ages: '))
     if age == 0:
          break
     ages.append(age)

for age in ages:
     if age <= 2:
          admission = 0.0
          print('admission is free enter')
     elif 3 <= age <= 12:
          admission += 14.0
          print('admission is $14 enter')
     elif age >= 65:
          admission += 18.0
          print('admission is $65 enter')
     else:
          admission += 23.0
          print('admission is $23 enter')
     

          

print(ages)
print(admission)


