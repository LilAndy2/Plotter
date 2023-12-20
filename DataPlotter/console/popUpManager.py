import PySimpleGUI as psg
from data_processing.point import Point
from console import consoleRunner

# ASPECT VARIABLES
layout_background_color = '#EBEBD3'
layout_text_color = '#5c574f'
title_font = ('Roboto', 20, 'bold')
text_font = 'Roboto'
button_background_color = '#210B2C'
button_highlight_color = '#55286F'
button_size = (10, 2)


def welcomePopUp():
    file = open("utils/OpenPopUpText.txt", "r")
    text = file.read()
    psg.popup_scrolled(text, title="Scrolled Popup", font=("Arial Bold", 16), size=(70, 10))


def addPointPopUp(processor):
    layout = [
        [psg.Text('X ', size=(10, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.Text('Y ', size=(10, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.Text('Add from file: ', size=(10, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'),
         psg.Input(size=(10, 1)),
         psg.FileBrowse(key="-IN-")],
        [psg.OK(button_color=button_background_color, font=text_font),
         psg.Cancel(button_color=button_background_color, font=text_font)]
    ]
    popup_window = psg.Window('Add', layout, size=(300, 300), background_color=layout_background_color)
    event, values = popup_window.read()

    if event == 'OK':
        if values["-IN-"] != '':
            file = open(values["-IN-"], "r")
            text = file.read()
            # read tuples of floats from each line
            tuples = [tuple(map(float, line.split())) for line in text.split('\n')]
            processor.add_list_points([Point(t[0], t[1]) for t in tuples])
        if values[0] != '' and values[1] != '':
            x, y = float(values[0]), float(values[1])
            processor.add_point(Point(x, y))

        print(processor.get_points())

        consoleRunner.updatePlot()

        popup_window.close()

    elif event == 'Cancel':
        popup_window.close()

    return None


def removePointPopUp(processor):
    layout = [
        [psg.Text('X ', size=(10, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.Text('Y ', size=(10, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.OK(button_color=button_background_color, font=text_font),
         psg.Cancel(button_color=button_background_color, font=text_font)]
    ]
    popup_window = psg.Window('Remove', layout, size=(200, 200), background_color=layout_background_color)
    event, values = popup_window.read()

    if event == 'OK':
        x, y = float(values[0]), float(values[1])
        if processor.pointCollection.points.count(Point(x, y)) > 0:
            processor.remove_point(Point(x, y))
        # Actualizați și afișați graficul în timp real în fereastra principală
        consoleRunner.updatePlot()
        popup_window.close()
    return None

