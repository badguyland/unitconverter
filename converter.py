import PySimpleGUI as sg


unit_conversions = {
    "Length": {
        "Inches": {"Centimeters": 2.54, "Feet": 1/12, "Yards": 1/36, "Meters": 0.0254, "Kilometers": 0.0000254, "Miles": 1.57828e-5},
        "Feet": {"Inches": 12, "Centimeters": 30.48, "Yards": 1/3, "Meters": 0.3048, "Kilometers": 0.0003048, "Miles": 0.000189394},
        "Yards": {"Inches": 36, "Feet": 3, "Centimeters": 91.44, "Meters": 0.9144, "Kilometers": 0.0009144, "Miles": 0.000568182},
        "Meters": {"Inches": 39.3701, "Feet": 3.28084, "Yards": 1.09361, "Centimeters": 100, "Kilometers": 0.001, "Miles": 0.000621371},
        "Kilometers": {"Inches": 39370.1, "Feet": 3280.84, "Yards": 1093.61, "Meters": 1000, "Miles": 0.621371},
        "Miles": {"Inches": 63360, "Feet": 5280, "Yards": 1760, "Meters": 1609.34, "Kilometers": 1.60934}
    },
    "Weight": {
        "Pounds": {"Ounces": 16, "Kilograms": 0.453592, "Grams": 453.592},
        "Ounces": {"Pounds": 1/16, "Kilograms": 0.0283495, "Grams": 28.3495},
        "Kilograms": {"Pounds": 2.20462, "Ounces": 35.274, "Grams": 1000},
        "Grams": {"Pounds": 0.00220462, "Ounces": 0.035274, "Kilograms": 0.001}
    },
    "Volume": {
    "Liters": {"Milliliters": 1000, "Gallons": 0.264172, "Quarts": 1.05669, "Pints": 2.11338},  # Added Pints conversion factor
    "Milliliters": {"Liters": 0.001, "Gallons": 0.000264172, "Quarts": 0.00105669, "Pints": 0.00211338},
    "Gallons": {"Liters": 3.78541, "Milliliters": 3785.41, "Quarts": 4, "Pints": 8},             # Added Pints conversion factor
    "Quarts": {"Liters": 0.946353, "Milliliters": 946.353, "Gallons": 0.25, "Pints": 0.5},        # Added Pints conversion factor
    "Pints": {"Liters": 0.473176, "Milliliters": 473.176, "Gallons": 0.125, "Quarts": 2}           # Added Pints conversion factor
}
}

def update_unit_options(window, selected_type):
    from_options = list(unit_conversions[selected_type].keys())
    window['-FROM-'].update(values=from_options)
    window['-TO-'].update(values=from_options)

layout = [
    [sg.Text('Enter value:'), sg.InputText()],
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
        break

    if event == 'Convert':
        value = float(values[0])
        conversion_type = values['-KIND-']
        from_unit = values['-FROM-']
        to_unit = values['-TO-']
        if from_unit == to_unit:
            converted_value = value
        else:
            conversion_factor = unit_conversions[conversion_type][from_unit][to_unit]
            converted_value = value * conversion_factor
        window['-OUTPUT-'].update(converted_value)

    if event == '-KIND-':
        selected_type = values['-KIND-']
        update_unit_options(window, selected_type)

window.close()
