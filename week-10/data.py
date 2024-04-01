import csv

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