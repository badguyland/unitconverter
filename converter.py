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
        "Liters": {"Milliliters": 1000, "Gallons": 0.264172, "Quarts": 1.05669, "Pints": 2.11338},
        "Milliliters": {"Liters": 0.001, "Gallons": 0.000264172, "Quarts": 0.00105669, "Pints": 0.00211338},
        "Gallons": {"Liters": 3.78541, "Milliliters": 3785.41, "Quarts": 4, "Pints": 8},
        "Quarts": {"Liters": 0.946353, "Milliliters": 946.353, "Gallons": 0.25, "Pints": 0.5},
        "Pints": {"Liters": 0.473176, "Milliliters": 473.176, "Gallons": 0.125, "Quarts": 2}
    },
    "Time": {
        "Nanoseconds": {"Microseconds": 0.001, "Milliseconds": 1e-6, "Seconds": 1e-9, "Minutes": 1.66667e-11, "Hours": 2.77778e-13, "Days": 1.15741e-14, "Weeks": 1.65344e-15, "Months": 3.80518e-16, "Years": 3.16888e-17},
        "Microseconds": {"Nanoseconds": 1000, "Milliseconds": 0.001, "Seconds": 1e-6, "Minutes": 1.66667e-8, "Hours": 2.77778e-10, "Days": 1.15741e-11, "Weeks": 1.65344e-12, "Months": 3.80518e-13, "Years": 3.16888e-14},
        "Milliseconds": {"Nanoseconds": 1e6, "Microseconds": 1000, "Seconds": 0.001, "Minutes": 1.66667e-5, "Hours": 2.77778e-7, "Days": 1.15741e-8, "Weeks": 1.65344e-9, "Months": 3.80518e-10, "Years": 3.16888e-11},
        "Seconds": {"Nanoseconds": 1e9, "Microseconds": 1e6, "Milliseconds": 1000, "Minutes": 0.0166667, "Hours": 2.77778e-4, "Days": 1.15741e-5, "Weeks": 1.65344e-6, "Months": 3.80518e-7, "Years": 3.16888e-8},
        "Minutes": {"Nanoseconds": 6e10, "Microseconds": 6e7, "Milliseconds": 60000, "Seconds": 60, "Hours": 0.0166667, "Days": 0.000694444, "Weeks": 9.9206e-5, "Months": 2.28311e-5, "Years": 1.90259e-6},
        "Hours": {"Nanoseconds": 3.6e12, "Microseconds": 3.6e9, "Milliseconds": 3.6e6, "Seconds": 3600, "Minutes": 60, "Days": 0.0416667, "Weeks": 0.00595238, "Months": 0.00136986, "Years": 0.000114155},
        "Days": {"Nanoseconds": 8.64e13, "Microseconds": 8.64e10, "Milliseconds": 8.64e7, "Seconds": 86400, "Minutes": 1440, "Hours": 24, "Weeks": 0.142857, "Months": 0.0328767, "Years": 0.00273973},
        "Weeks": {"Nanoseconds": 6.048e14, "Microseconds": 6.048e11, "Milliseconds": 6.048e8, "Seconds": 604800, "Minutes": 10080, "Hours": 168, "Days": 7, "Months": 0.229985, "Years": 0.019165},
        "Months": {"Nanoseconds": 2.63e15, "Microseconds": 2.63e12, "Milliseconds": 2.63e9, "Seconds": 2.63e6, "Minutes": 43829.1, "Hours": 730.484, "Days": 30.4368, "Weeks": 4.34524, "Years": 0.0833333},
        "Years": {"Nanoseconds": 3.15e16, "Microseconds": 3.15e13, "Milliseconds": 3.15e10, "Seconds": 3.15e7, "Minutes": 525600, "Hours": 8760, "Days": 365, "Weeks": 52.1429, "Months": 12}
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
        print ("Shutting down...")
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
