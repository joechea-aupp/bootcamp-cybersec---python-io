with open('students_scores.txt', 'r') as file:
    student_data = file.readlines()
    student_scores = []

    for student in student_data:
        student_scores.append(int(student.split(':')[1].strip()))

    print('there are {} get lowest score of {}'.format( student_scores.count(min( student_scores )), min( student_scores )))

    print('there are {} get maximum score of {}'.format( student_scores.count(max( student_scores )), max( student_scores )))

    print('average student score {}'. format(sum(student_scores)/len(student_scores)))


    # get number of student that has score above average
    above_average = 0
    for score in student_scores:
        if score > sum(student_scores)/len(student_scores):
            above_average += 1

    print('there are {} students that has score above average'.format(above_average))
