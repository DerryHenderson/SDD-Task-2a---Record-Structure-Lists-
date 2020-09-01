#Task 2a
#Derry Henderson

student = []

student.append(input('Please enter name: '))

student.append(float(input('Please enter age:')))

studentage = student[1]

while not studentage.is_integer():
  studentage = float(input("Please enter age:   "))
  
while studentage <1 or studentage >150:
  student[1] = float(input('Please enter age: '))

student[1] = int(studentage)


student.append(float(input('Please enter height: ')))

while student[2] <1 or student[2] >2.5:
  student[2] = (float(input('Please enter height: ')))

student.append(input('What is your home town?: '))

print(student)