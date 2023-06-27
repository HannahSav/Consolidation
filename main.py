import PySimpleGUI as sg
import logging
from DB_sending import *
from parsing import *

layout = [
    [sg.Text('Choose directory to enter files into DataBase')],
    [sg.Text('Directory'), sg.InputText(), sg.FolderBrowse()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Files upload', layout)

while True:  # The Event Loop
    event, values = window.read()
    print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event in 'Submit':
        if (values[0] == ''):
            print('upload the file, please')
        else:
            print('uploaded it')
            parsing_directory(values[0])