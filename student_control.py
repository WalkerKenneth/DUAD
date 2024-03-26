import csv


def get_menu_value():
    selection = 0
    print(
        """
        Student Control Panel

            1) Add Student
            2) See all students data
            3) Top 3 students
            4) All students average
            5) Export student data to csv
            6) Import data from csv
        """
    )
    while True:
        try:
            selection = int(input('Select an option from the menu "Press 7 to exit": '))
            if selection < 1 or selection > 7:
                raise ValueError()
            break
        except ValueError as ex:
            print ('Invalid selection')
    return selection


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


def create_student(headers):
    student = {}
    for element in headers:
        for key in element:
            if key == 'name' or key == 'group':
                student[key] = input(f'Student {element[key]}: ')
            else:
                student[key] = get_student_note(element[key] + ': ')
    return student


def create_student_list():
    student_list = []
    headers = [
        {'name': 'Name'},
        {'group': 'Group'},
        {'spanish_note':'Spanish note'},
        {'english_note':'English note'},
        {'history_note':'History note'},
        {'science_note':'Science note'},
        ]
    while True:
        student_list.append(create_student(headers))
        stop = input('Stop to add students (Y/N)')
        if stop == 'Y' or stop == 'y':
            break
    return student_list


def show_student_data(student_list):
    print('Student Data')
    for student in student_list:
        print(student['name'] + ' - Group ' + student['group'])
        print(
            'Spanish note: ' + str(student['spanish_note']) + ' ' +
            'English note: ' + str(student['english_note']) + ' ' +
            'History note: ' + str(student['history_note']) + ' ' +
            'Science note: ' + str(student['science_note']) + ' ' +
            '\n--------'
        )


def get_average(student):
    return (student['spanish_note'] +
            student['english_note'] +
            student['history_note'] +
            student['science_note']
    ) / 4


def get_top_student(list, student_number):
    top_student = []

    try:
        for student in list:
            student_average = {'name':student['name'],'average':get_average(student)}
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


def export_data(list):
    headers = []
    try:
        for key in list[0]:
            headers.append(key)
    except IndexError as ex:
        print('Incorrect list provided')
    with open('student_list.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(list)


def import_data():
    student_list = []
    try:
        with open('student_list.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key in row:
                    if key[len(key)-4:len(key)] == 'note':
                        row[key] = int(row[key])
                student_list.append(row)
    except FileNotFoundError:
        print('Document is not available')
    return student_list


def main():
    student_list = []
    operator = 0
    while True:
        operator = get_menu_value()
        if operator == 1:
            student_list.extend(create_student_list())
        elif operator == 2:
            show_student_data(student_list)
        elif operator == 3:
            show_top_students(student_list)
        elif operator == 4:
            show_all_students_average(student_list)
        elif operator == 5:
            export_data(student_list)
        elif operator == 6:
            student_list = import_data()
        elif operator == 7:
            break


if __name__=='__main__':
    main()