import csv
from student import Student

def import_data():
    student_list = []
    try:
        with open('week-10/student_list.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key in row:
                    if key[len(key)-4:len(key)] == 'note':
                        row[key] = int(row[key])
                student_list.append(Student(
                    row['name'],
                    row['group'],
                    row['spanish_note'],
                    row['english_note'],
                    row['history_note'],
                    row['science_note']
                ))
    except FileNotFoundError:
        print('Document is not available')
    return student_list


def export_data(person_list):
    list = []
    headers = [
        'name',
        'group',
        'spanish_note',
        'english_note',
        'history_note',
        'science_note'
    ]
    for person in person_list:
        list.append(
            {
                'name': person.name,
                'group': person.group,
                'spanish_note': person.spanish_note,
                'english_note': person.english_note,
                'history_note': person.history_note,
                'science_note': person.science_note
            }
        )

    with open('week-10/student_list.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(list)