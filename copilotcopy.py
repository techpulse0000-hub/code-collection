grade = []
total = 0.0
new = []



while True:
    G = input('input you grade to calculate the average: (blank to quit) ')
    if G == '':
          break
    new.append(total)
    grade.append(G)

for G in grade:
     if grade == 'A+':
         total += 4.0
     elif 'A-':
         total += 3.7
     elif grade == 'B+':
          total += 3.3
     elif grade == 'B+':
         total += 3.3
     elif grade == 'B':
         total += 3.0
     elif grade == 'B-':
         total += 2.7
     elif grade == 'C+':
         total += 2.3
     elif G == 'C':
         total = total + 2.0
     elif G == 'C-':
         total = total + 1.7
     elif G == 'D+':
         total = total + 1.3
     elif G == 'D':
         total = total + 1.0
     elif G == 'F':
         total = total + 0

             
     
     else:
          total += 4.0
     

          

print(grade)
print(total/len(new))



