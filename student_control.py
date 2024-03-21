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
                raise ValueError('Invalid selection')
            break
        except ValueError as ex:
            print (ex)
    return selection


def create_student(headers):
    student = {}
    for element in headers:
        for key in element:
            student[key] = input(f'Student {element[key]}: ')
    print(student)
    return student


def main():
    student_list = []
    operator = 0
    headers = [
        {'name': 'Name'},
        {'group': 'Group'},
        {'spanish_note':'Spanish note'},
        {'english_note':'English note'},
        {'history_note':'History note'},
        {'science_note':'Science note'},
    ]
    # while True:
    operator = get_menu_value()
    if operator == 1:
        student_list.append(create_student(headers))


if __name__=='__main__':
    main()