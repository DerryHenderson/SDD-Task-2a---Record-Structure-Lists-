#Task 2a
#Derry Henderson

#create student list
student = []

#receive student name and add to list
student.append(input('Please enter name: '))

#receive student age and add to list
student.append(float(input('Please enter age:')))

#validate age as a whole number between 1 and 150
while student[1] <1 or student[1] >150 or not student[1].is_integer():
  student[1] = float(input('Please enter age: '))

student[1] = int(student[1])

#receive student height and add to list
student.append(float(input('Please enter height: ')))

#validate height to be between 1 and 2.5
while student[2] <1 or student[2] >2.5:
  student[2] = (float(input('Please enter height: ')))

#receive student age and add to list
student.append(input('What is your home town?: '))

#print student info
print(student)