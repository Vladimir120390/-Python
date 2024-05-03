grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average_grades = [sum(grade) / len(grade) for grade in grades]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
new_students = sorted(students)
print()
grade_student = zip(new_students, average_grades)
print("Cредний балл студента: ", dict(grade_student))


