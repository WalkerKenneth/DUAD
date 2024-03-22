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
            7) Close
        """
    )
    while True:
        try:
            selection = int(input('Select an option from the menu "Press 7 to exit": '))
            if selection < 1 or selection > 7:
                raise ValueError('Invalid selection')
            break
        except ValueError as ex:
            print (ex)
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
            show_student_data(student_list)
        elif operator == 2:
            show_student_data(student_list)
        elif operator == 2:
            show_student_data(student_list)
        elif operator == 2:
            show_student_data(student_list)
        elif operator == 7:
            break


if __name__=='__main__':
    main()