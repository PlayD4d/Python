import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Text v řádku 1')],
            [sg.Text('Napiš něco do řádku 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Zrušit')] ]

# Create the Window
window = sg.Window('Název okna', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Zrušit': # if user closes window or clicks cancel
        break
    sg.popup('Napsal jsi ', values[0])

window.close()
