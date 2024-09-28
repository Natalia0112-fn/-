#student = []
#student.append ('Denis')
#student.append('Adam')
#student.append('Valentin')
#print(student)
#sort_student = sorted(student)
#print(sort_student)

student = {"Denis", "Adam", "Valentin"}
sort_student = sorted(student)
grades = [[3,5,5,2,4], [5,3,5,4,3], [4,4,4,3,3]]
grades_1 = [sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2])]
student_1 = dict(zip(sort_student, grades_1))
print(student_1)








