import PySimpleGUI as sg

sg.theme('black')
layout = [
    [sg.Image('/Users/vihan/Desktop/10 Apps/stopwatch/cross.png')],
    [sg.VPush()],
    [sg.Text('time')],
    [sg.Button('Start'),sg.Button('Lap')],
    [sg.VPush()]
]

window = sg.Window(
    'Stopwatch',
    layout,
    size = (300,300),
    no_titlebar = True,
    element_justification = 'center')

while True:
    event, values = window.read()
    if event == (sg.WIN_CLOSED, 'Start'):
        break

window.close()