import PySimpleGUI as psg
from data_processing.point import Point
from data_processing.processorAPI import ProcessorAPI
from matplotlib import pyplot as plt
import os


def welcomePopUp():
    file = open("utils/OpenPopUpText.txt", "r")
    text = file.read()
    psg.popup_scrolled(text, title="Scrolled Popup", font=("Arial Bold", 16), size=(70, 10))

puncte = []

# Numele fișierului PNG
nume_fisier_png = 'grafic.png'

# Variabilă pentru a ține evidența dacă legenda a fost deja adăugată
legenda_adaugata = False

def updatePlot():
    global legenda_adaugata
    fig, ax = plt.subplots()

    # Adăugare toate punctele existente
    for p in puncte:
        ax.scatter(p.x, p.y, color='red', marker='o', label='Punct')

    #canvas = FigureCanvasTkAgg(figure, window['-CANVAS-'].Widget)
    #canvas.draw()
    #canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    # Adăugare detalii axelor, etichetelor etc.
    ax.set_title('Reprezentarea Punctelor')
    ax.set_xlabel('Coordonata X')
    ax.set_ylabel('Coordonata Y')

    # Adăugare rețea pe axă
    ax.grid(True)

    # Salvare și actualizare imagine PNG
    plt.savefig(nume_fisier_png)
    plt.draw()

    # Adăugare legenda (doar dacă nu a fost deja adăugată)
    if not legenda_adaugata:
        ax.legend()
        legenda_adaugata = True

    # Afișare grafic în fereastră
    plt.show()


puncte = []

def addPointPopUp():
    psg.set_options(font=('Arial Bold', 16))
    layout = [
        [psg.Text('X ', size=(10, 1)), psg.Input(expand_x=True)],
        [psg.Text('Y ', size=(10, 1)), psg.Input(expand_x=True)],
        [psg.OK(), psg.Cancel()]
    ]
    popup_window = psg.Window('Add Point', layout, size=(200, 200))
    event, values = popup_window.read()

    if event == 'OK':
        x, y = float(values[0]), float(values[1])
        point = Point(x, y)
        puncte.append(point)

        # Actualizați și afișați graficul în timp real în fereastra principală
        updatePlot()


        popup_window.close()

        return point

    return None

def removePointPopUp():
    global puncte  # Declară variabila puncte ca fiind globală pentru a o putea modifica în funcție
    psg.set_options(font=('Arial Bold', 16))
    layout = [
        [psg.Text('X ', size=(10, 1)), psg.Input(expand_x=True)],
        [psg.Text('Y ', size=(10, 1)), psg.Input(expand_x=True)],
        [psg.OK(), psg.Cancel()]
    ]
    window = psg.Window('Form', layout, size=(200, 200))
    event, values = window.read()
    window.close()

    if event == 'OK':
        x, y = float(values[0]), float(values[1])
        point = Point(x, y)
        if point in puncte:
             puncte.remove(point)
        else:
            print("punct inexistent")
            return None

        # Actualizare și afișare grafic în timp real
        updatePlot()

        return point

    return None

def integralPopUp(processor):
    psg.set_options(font=('Arial Bold', 16))
    layout = [
        [psg.Text('Left Bound: ', size=(10, 1)), psg.Input(expand_x=True)],
        [psg.Text('Right Bound: ', size=(10, 1)), psg.Input(expand_x=True)],
        [psg.Text('Accuracy: ', size=(10, 1)), psg.Input(expand_x=True)],
        [psg.OK(), psg.Cancel()]
    ]
    window = psg.Window('Form', layout, size=(200, 200))
    event, values = window.read()
    print(event, values)
    window.close()
    if event == 'OK':
        return processor.integrate(values[0], values[1], values[2])
    return None
