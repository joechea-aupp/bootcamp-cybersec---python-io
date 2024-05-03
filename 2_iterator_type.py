from collections.abc import Iterable

with open('students_scores.txt', 'r') as file:
    print('is iterator? :', isinstance(file, Iterable))

    student_data_list = file.readlines()

    for student in student_data_list:
        student_list = student.split(':')
        print('Student Name: {} and Score: {}'.format(student_list[0], student_list[1]))







