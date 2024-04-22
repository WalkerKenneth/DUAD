import PySimpleGUI as sg
import data
from add_menu import AddMenu
from category import Category

class PrincipalMenu:

    def __init__(self) -> None:
        self.headings = ['I/E', 'Detail', 'Category', 'Amount']
        self.values = data.import_values()
        self.category = Category().category_list

        table = sg.Table(headings=self.headings, values=self.values, key='-TABLE-')
        layout = [  
            [sg.Text('Income/Expense Record')],
            [table],
            [sg.Button('Add Income'), sg.Button('Add Expense'), sg.Button('Add Category')],
        ]
        window = sg.Window('Personal Finance', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Add Income':
                values_to_add = AddMenu('Income', self.category).data
                if values_to_add is not None:
                    self.values.append(values_to_add)
                    data.export_values(self.values)

            elif event == 'Add Expense':
                values_to_add = AddMenu('Expense', self.category).data
                if values_to_add is not None:
                    self.values.append(values_to_add)
                    data.export_values(self.values)

            elif event == 'Add Category':
                category_to_add = Category().add_category()
                if category_to_add not in self.category:
                    self.category.append(category_to_add)
                    data.export_category(self.category)
                else:
                    sg.popup('Category already included in the Database')

            window['-TABLE-'].update(values=self.values)

        window.close()