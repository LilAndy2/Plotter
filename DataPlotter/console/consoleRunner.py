import PySimpleGUI as psg
from data_processing import processorAPI
import console.popUpManager as popUp


def runner():
    layout = [[psg.Text(text='Hello World',
                        font=('Arial Bold', 20),
                        size=20,
                        expand_x=True,
                        justification='center')],
              ]
    popUp.welcomePopUp()
    window = psg.Window('HelloWorld', layout, size=(700, 700))
    while True:
        event, values = window.read()
        print(event, values)
        if event in (None, 'Exit'):
            break
    window.close()
