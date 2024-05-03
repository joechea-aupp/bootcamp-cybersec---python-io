with open('students_scores.txt', 'r') as file:
    student_data_str = file.read()
    print(type(student_data_str))

    student_data_one = file.readline()
    print(type(student_data_one))

    student_data_list = file.readlines()
    print(type(student_data_list))

    # print(student_data_one)
    # print(student_data_list)








