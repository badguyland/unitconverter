import PySimpleGUI as sg
from conversions import unit_conversions




def update_unit_options(window, selected_type):
    from_options = list(unit_conversions[selected_type].keys())
    window['-FROM-'].update(values=from_options)
    window['-TO-'].update(values=from_options)

layout = [
    [sg.Text('Enter value:'), sg.InputText(key = '-INPUT-')],
    [sg.Text('Type:'), sg.Combo(list(unit_conversions.keys()), key='-KIND-', enable_events=True)],
    [sg.Text('From:'), sg.Combo([], key='-FROM-', size=(20, 20))],
    [sg.Text('To:'), sg.Combo([], key='-TO-', size=(20, 20))],
    [sg.Button('Convert')],
    [sg.Text('Converted value:'), sg.Text(size=(15,1), key='-OUTPUT-')],
    [sg.Button('Quit')] 
]

window = sg.Window('Unit Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        print ("Shutting down...")
        break

    if event == 'Convert':
        try:
            value = float(values['-INPUT-'])
            conversion_type = values['-KIND-']
            from_unit = values['-FROM-']
            to_unit = values['-TO-']
            if from_unit == to_unit:
                converted_value = value
            else:
                conversion_factor = unit_conversions[conversion_type][from_unit][to_unit]
                converted_value = value * conversion_factor
            window['-OUTPUT-'].update(converted_value)
        except (ValueError, KeyError) :
            sg.Popup("Input Error") 

    if event == '-KIND-':
        selected_type = values['-KIND-']
        update_unit_options(window, selected_type)

window.close()
