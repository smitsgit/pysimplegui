import PySimpleGUI as sg
cols = [
    [sg.Text('Search Key', size=(15,1),text_color='white'),
 sg.Input('', key='search1', enable_events=True)],

 [sg.Listbox(values=('Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'), key='lst',
             select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(60,4), enable_events=False)],

[sg.Text('App Id', size=(15,1), text_color='white'),
 sg.Input('', key='search2', enable_events=True)],

[sg.Text('App Version', size=(15,1), text_color='white', background_color='blue'),
 sg.Input('', key='search3', enable_events=True)],

[sg.Multiline(default_text='', size=(60, 5),
                        font='Any 16')],

[sg.OK(), sg.Cancel()]

        ]

def main():
    # window = sg.Window('Get filename example', resizable=True, layout=layout, font=('',16))
    window = sg.Window('Get filename example', resizable=True, font=('',16)).Layout([[sg.Column(cols, size=(700,400), scrollable=True)]])

    while True:
        event, values = window.read()
        print("=====>", event, values)
        # window['lst'].update(values = ["Hello", "world"])
        if event in ['OK', sg.WIN_CLOSED]:
            break
    window.close()


if __name__ == '__main__':
    main()