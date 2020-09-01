#Task 2a
#Derry Henderson

student = []

student.append(input('Please enter name: '))

student.append(float(input('Please enter age:')))
  
while student[1] <1 or student[1] >150 or not student[1].is_integer():
  student[1] = float(input('Please enter age: '))

student[1] = int(student[1])


student.append(float(input('Please enter height: ')))

while student[2] <1 or student[2] >2.5:
  student[2] = (float(input('Please enter height: ')))

student.append(input('What is your home town?: '))

print(student)