import PySimpleGUI as psg
from data_processing.processorAPI import ProcessorAPI
import console.popUpManager as popUp


# console should be able to:
# - add points to the dataset (using addPointPopUp in popUpManager)
# - remove points from the dataset
# - trigger the calculation of the polynomial function
# - trigger the extrapolation of a point
# - change the mode of the dataset (line, dtm, none)
# - display the dataset
# - display the polynomial function
# - display the extrapolated point
# - trigger the calculation of the integral of the polynomial function
#
# Needed buttons:
# - add/remove points (select between add point, add multiple points from file, remove point)
# - calculate integral/derivative (select between them - change the mode of the api to line)
# - linreg (change the mode of the api to line)
# - see next predicted point (change the mode of the api to dtm)
# - extrapolate point (change the mode of the api to line)
#
# Data displaying:
# - when mode is none, display the points
# - when mode is line, display the points and the polynomial function
# - when mode is dtm, display the points

import PySimpleGUI as psg
from data_processing.processorAPI import ProcessorAPI
import console.popUpManager as popUp

def addPointPopUp_from_button():
    # Funcția care va fi apelată la apăsarea butonului "Button One"
    popUp.addPointPopUp()

def runner():
    # Definirea aspectului ferestrei cu un element Text și un buton
    layout = [
        [psg.Text(text='Hello World',
                  font=('Arial Bold', 20),
                  size=20,
                  expand_x=True,
                  justification='center')],
        [psg.Button('Add Point', key='-BUTTON_ONE-')],
    ]

    # Crearea ferestrei PySimpleGUI
    window = psg.Window('HelloWorld', layout, size=(700, 700))

    # Crearea unei instanțe ProcessorAPI
    processor = ProcessorAPI()

    # Bucla principală de evenimente
    while True:
        event, values = window.read()

        if event in (None, 'Exit'):
            break
        elif event == '-BUTTON_ONE-':
            # Apelarea funcției când este apăsat butonul "Button One"
            addPointPopUp_from_button()

    # Închiderea ferestrei la finalul buclei
    window.close()

if __name__ == '__main__':
    runner()

