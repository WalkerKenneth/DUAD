from student import Student

def get_student_note(text):
    note = 0
    while True:
        try:
            note = int(input(text))
            if note < 0 or note > 100:
                raise ValueError()
            return note
        except ValueError as ex:
            print('Invalid note')


def create_student():
    return Student (
        input('Student Name: '),
        input('Student Group: '),
        get_student_note('Spanish: '),
        get_student_note('English: '),
        get_student_note('History: '),
        get_student_note('Science: '),
    )


def create_student_list():
    student_list = []
    while True:
        student_list.append(create_student())
        stop = input('Stop to add students (Y/N)')
        if stop == 'Y' or stop == 'y':
            break
    return student_list


def show_student_data(student_list):
    print('Student Data')
    for student in student_list:
        print(student.name + ' - Group ' + student.group)
        print(
            'Spanish note: ' + str(student.spanish_note) + ' ' +
            'English note: ' + str(student.english_note) + ' ' +
            'History note: ' + str(student.history_note) + ' ' +
            'Science note: ' + str(student.science_note) + ' ' +
            '\n--------'
        )


def get_average(student):
    return (student.spanish_note +
            student.english_note +
            student.history_note +
            student.science_note
    ) / 4


def get_top_student(list, student_number):
    top_student = []

    try:
        for student in list:
            student_average = {'name':student.name,'average':get_average(student)}
            if len(top_student) == 0:
                top_student.append(student_average)
            else:
                for best_student in top_student:
                    if student_average['average'] > best_student['average']:
                        top_student.insert(top_student.index(best_student), student_average)
                        break
                    elif (len(top_student) < student_number):
                        top_student.append(student_average)
                if len(top_student) > student_number:
                    top_student.pop()
    except IndexError:
        print('No more student in the data base: Index Error')
    except KeyError:
        print('No more student in the data base: Key Error')
    except ValueError:
        print('No more student in the data base: Value Error')
    return top_student


def show_top_students(student_list):
    top_student = get_top_student(student_list, 3)
    print('Top students')
    for best_student in top_student:
        print(
            f'{best_student['name']}: Average: {best_student['average']}'
        )


def show_all_students_average(list):
    total_average = 0
    for student in list:
        total_average += get_average(student)
    try:
        total_average = total_average / len(list)
    except ZeroDivisionError:
        print('No students registered: ZeroDivisionError')
    print(f'All students average: {total_average}')