import PySimpleGUI as sg
import data

class Category:

    def __init__(self) -> None:
        self.category_list = self.load_list()


    def load_list(self):
        return data.import_category()


    def add_category(self):
        layout = [
            [sg.Text('Category Name'), sg.InputText()],
            [sg.Button('Add Category')]
        ]
        window = sg.Window('Add Category', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            elif event == 'Add Category':
                window.close()
                if values[0] != '':
                    return values[0]