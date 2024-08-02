#def input():
students = []





#taking data from user
ind_st_data = []
for st in range(3):
  student = input(" Enter your name:")
  ind_st_data.append(student)
  #students.append(student)
for c in range (0,4):
  course = input("What is your course:")
  ind_st_data.append(course)
  
for s in range(0,4):
   score = int(input("What is your score:"))
   ind_st_data.append(score)

def ind_st_data():
 return ind_st_data
print(ind_st_data())

   #scores.append(score)
for students in range(0,4):
 students.append(ind_st_data)

 print(students)

 #return student,course,score
#def result():
  #print(students)

#result

#displaying results
# def result(student, course, score):
#   print(f"{student}",f"{course}",f"{score}")

# #executing the functions
# student,course,score = user_input()
# result(student=student, course=course, score=score) 
#print(students) 