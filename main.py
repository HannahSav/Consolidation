import PySimpleGUI as sg
import logging
from DB_sending import *
from parsing import *

layout = [
    [sg.Text('Choose file to enter it in DataBase')],
    [sg.Text('File'), sg.InputText(), sg.FileBrowse()],
    # [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]

layout_error = [
    [sg.Text('Format should be as .xlsx')],
    [sg.Cancel()]
]

window = sg.Window('File Compare', layout)

while True:  # The Event Loop
    event, values = window.read()
    print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event in 'Submit':
        print('Submit file')
        logging.info('Submit the file')
        print('values =', values[0][-5:])
        if (values[0] == ''):
            print('upload the file, please')
        elif (values[0][-5:] != '.xlsx'):
            print('File should be an xlsx format')
        else:
            print('uploaded it')
            parsing_file(values[0])
       # load it openpyxl
else:
    print(filename, "is an CSV file!")