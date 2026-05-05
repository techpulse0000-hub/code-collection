import numpy as np

scores = np.array([
[78, 85, 90, 67, 88],          #the students scores, subject, by column and student by row
[56, 72, 80, 69, 75],
[90, 91, 89, 94, 92],
[45, 60, 55, 58, 62],
[88, 79, 84, 91, 87],
[67, 73, 70, 65, 68],
[92, 95, 94, 96, 93],
[74, 81, 78, 76, 80],
[59, 64, 61, 63, 60],
[83, 86, 85, 88, 84],
[71, 75, 72, 70, 73],
[66, 68, 65, 67, 69],
[89, 92, 90, 91, 93],
[52, 58, 55, 57, 54],
[77, 80, 79, 78, 81],
[61, 65, 63, 60, 62],
[94, 96, 95, 97, 98],
[69, 72, 70, 68, 71],
[85, 88, 87, 86, 89],
[73, 76, 74, 72, 75]
])


avg = np.mean(scores, axis=1)

print(f"student average: {avg}")
print(f"Best student: student {np.argmax(avg)+1}; score:{max(avg)}") 
print(f"worst student: student {np.argmin(avg)+1}; score: {min(avg)}")
print(f"the average of the class is {np.mean(avg)}") 

subject_avg = np.mean(scores, axis=0)

print(f"hardest subject: subject {np.argmin(subject_avg)}")