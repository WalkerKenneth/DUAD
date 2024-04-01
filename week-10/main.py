from data import import_data, export_data
from menu import get_menu_value
from actions import create_student_list, show_student_data, show_top_students, show_all_students_average


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