import PySimpleGUI as sg
import tkinter as tk
layout = [
    [sg.Text('input1'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('Check1'), sg.Checkbox('Check2')
     ],
    [sg.Text('input2'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('Check3')
     ],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]


import PySimpleGUI as sg
import re
import hashlib
def make_msg(checkbox):
    if checkbox == 'Check1':
        msg = 'Chek1 was chosen'
    elif checkbox == 'Check2':
        msg = "Chek2 was chosen"
    elif checkbox == 'Check3':
        msg = "Chek3 was chosen"
    
window = sg.Window('File Compare', layout)
while True:                             # The Event Loop
    event, values = window.read()
    
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        if values[0] and values[3]:
            input1 = values[0]
            input2 = values[3]
            
            
            
            if values[1] is not True and values[2] is not True and values[4] is not True:
                print('Error: Choose at least one Checkbox')
            
    print(input1,input2)           




