#Average heights
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#summaatory variable create to storage the
summatory = 0
studentsNumber = 0

#self-made length
for student in student_heights:
  studentsNumber += 1
#inputting values from the list inside the variable
for height in range(0, studentsNumber):
  summatory += student_heights[height]
#some mathematical struff
roundedValue = round(summatory / studentsNumber)

print(roundedValue)
