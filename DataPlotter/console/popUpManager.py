import PySimpleGUI as psg
from data_processing.point import Point
from data_processing.processorAPI import ProcessorAPI


def welcomePopUp():
    file = open("utils/OpenPopUpText.txt", "r")
    text = file.read()
    psg.popup_scrolled(text, title="Scrolled Popup", font=("Arial Bold", 16), size=(70, 10))


def addPointPopUp():
    psg.set_options(font=('Arial Bold', 16))
    layout = [
        [psg.Text('X ', size=(10, 1)), psg.Input(expand_x=True)],
        [psg.Text('Y ', size=(10, 1)), psg.Input(expand_x=True)],
        [psg.OK(), psg.Cancel()]
    ]
    window = psg.Window('Form', layout, size=(200, 200))
    event, values = window.read()
    print(event, values)
    window.close()
    if event == 'OK':
        return Point(values[0], values[1])
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
