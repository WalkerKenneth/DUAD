import PySimpleGUI as sg


class AddMenu:
    def __init__(self, type, category) -> None:
        self.type = type
        self.data = None
        layout = [
            [sg.Text(f'Add {self.type} Menu')],
            [sg.Text('Detail: '), sg.InputText()],
            [sg.Text('Category: '), sg.InputText()],
            [sg.Text('Amount: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

        window = sg.Window(f'{self.type}', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            elif event == 'Ok':
                try:
                    if values[0] == '' or  values[1] == '' or values[2] == '':
                        raise Exception()
                    else:
                        if values[1] in category:
                            try:
                                self.data = [self.type[0], values[0], values[1], int(values[2])]
                                break
                            except ValueError:
                                sg.popup('Please use a valid amount')
                        else:
                            sg.popup('Please use a valid category')
                except Exception:
                    sg.popup('Required data was not provided')
        window.close()