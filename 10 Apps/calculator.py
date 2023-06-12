import PySimpleGUI as sg

def create_window(theme):
    sg.theme('theme')
    sg.set_options(font = 'Franklin 14', button_element_size = (6,3))
    button_size = (6,3)
    layout = [
        [sg.Text(
            '',
            font = 'Franklin 26',
            justification = 'right',
            expand_x = True,
            pad = (10,20),
            right_click_menu = theme_menu,
            key = '-TEXT-')
                ],
        [sg.Button('Clear', expand_x = True), sg.Button('Enter', expand_x = True)],
        [sg.Button(7),sg.Button(8),sg.Button(9),sg.Button('*')],
        [sg.Button(3),sg.Button(5),sg.Button(6),sg.Button('/')],
        [sg.Button(1),sg.Button(2),sg.Button(3),sg.Button('x')],
        [sg.Button(0, expand_x = True),sg.Button('-'),sg.Button('+')],
    ]
        
    return sg.Window('Calculator', layout)

theme_menu = ['menu',['LightGrey1','dark','DarkGray8','random']]
window = create_window('dark')

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        
        if event in ['0','1','2','3','4','5','6','7','8','9','.']:
            current_num.append(event)
            num_string = ''.join(current_num)
            window['-TEXT-'].update(num_string)
    
    if event in ['+','-',',','/','*']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        print(full_operation)
        window['-TEXT-'].update('')

    if event == 'Enter':
        full_operation.append(''.join(current_num))
        result = eval((''.join(full_operation)))
        window['-TEXT-'].update(result)
        full_operation = []

    if event == 'Clear':
        current_num = []
        full_operation = []
        window['-TEXT'].update('')

window.close()