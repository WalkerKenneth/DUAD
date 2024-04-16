import csv

def import_category():
    category = []
    try:
        with open('category.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category.append(row['category'])
    except FileNotFoundError:
        pass
    return category


def export_category(category_list):
    list = []
    for category in category_list:
        list.append(
            {
                'category': category
            }
        )

    with open('category.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, ['category'])
        writer.writeheader()
        writer.writerows(list)


def import_values():
    values = []
    try:
        with open('values.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                values.append([
                    row['I/E'],
                    row['Detail'],
                    row['Category'],
                    row['Amount'],
                ])
    except FileNotFoundError:
        pass
    return values


def export_values(value_list):
    list = []
    for value in value_list:
        list.append(
            {
                'I/E': value[0],
                'Detail': value[1],
                'Category': value[2],
                'Amount': value[3]
            }
        )

    with open('values.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, ['I/E', 'Detail', 'Category', 'Amount'])
        writer.writeheader()
        writer.writerows(list)