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



def create_student(headers):
    student = {}
    for element in headers:
        for key in element:
            if key == 'name' or key == 'group':
                student[key] = input(f'Student {element[key]}: ')
            else:
                student[key] = get_student_note(element[key] + ': ')
    return student


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


def show_student_data(student_list):
    print(student_list)
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


def show_top_students(student_list):
    student_average = []
    for student in student_list:
        student_average.append({'name':student['name'], 'average':get_average(student)})
    top_student = get_top_student(student_average)
    for best_student in top_student:
        print(
            f'{best_student['name']}: Average: {best_student['average']}'
        )


def get_average(student):
    return (student['spanish_note'] + 
            student['english_note'] +
            student['history_note'] +
            student['science_note']
    ) / 4


def get_top_student(list):
    average_list = list.copy()
    top_3_student = []
    try:
        for student in range(0,3):
            best_student = {'name':'','average':0}
            for average in average_list:
                if average['average'] > best_student['average']:
                    best_student = average
            top_3_student.append(best_student)
            average_list.remove(best_student)
    except IndexError as ex:
        print('No more student in the data base: Index Error')
    except KeyError as ex:
        print('No more student in the data base: Key Error')
    return top_3_student


def show_all_students_average(list):
    total_average = 0
    for student in list:
        total_average += get_average(student)
    total_average = total_average / len(list)
    print(f'All students average: {total_average}')


def export_data(list):
    headers = []
    try:
        for key in list[0]:
            headers.append(key)
    except IndexError as ex:
        print('Incorrect list provided')

    with open('student_list.txt', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(list)


def import_data():
    student_list = []
    try:
        with open('student_list.txt', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
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