import PySimpleGUI as psg
from data_processing.processorAPI import ProcessorAPI
import console.popUpManager as popUp
import PySimpleGUI as psg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

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

# ASPECT VARIABLES
layout_background_color = '#EBEBD3'
layout_text_color = '#5c574f'
title_font = ('Roboto', 20, 'bold')
text_font = 'Roboto'
button_background_color = '#210B2C'
button_highlight_color = '#55286F'
button_size = (10, 2)

processor = ProcessorAPI()

primary_layout = [
    [
        psg.Text(text='Proiect', font=title_font, expand_x=True, justification='center', text_color=layout_text_color,
                 background_color=layout_background_color)
    ],
    [
        psg.Button('Add Point', key='-BUTTON_ADD_POINT-', size=button_size, button_color=button_background_color,
                   mouseover_colors=button_highlight_color, font=text_font, border_width=5),
        psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-', size=button_size, button_color=button_background_color,
                   mouseover_colors=button_highlight_color, font=text_font, border_width=5),
        psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-', size=button_size,
                   button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                   border_width=5),
        psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-', size=button_size,
                   button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                   border_width=5),
        psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-', size=button_size,
                   button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                   border_width=5),
    ],
    [
        psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-', size=button_size,
                   button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                   border_width=5),
        psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-', size=button_size,
                   button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                   border_width=5),
        psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-', size=button_size,
                   button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                   border_width=5),
    ],
    [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))]
]

def draw_figure(canvas, figure):
    tkcanvas = FigureCanvasTkAgg(figure, canvas)
    tkcanvas.draw()
    tkcanvas.get_tk_widget().pack(side='top', fill='both', expand=1)
    return tkcanvas

def updatePlot():
    primary_layout = [
        [
            psg.Text(text='Proiect', font=title_font, expand_x=True, justification='center',
                     text_color=layout_text_color, background_color=layout_background_color, border_width=5)
        ],
        [
            psg.Button('Add Point', key='-BUTTON_ADD_POINT-', size=button_size, button_color=button_background_color,
                       mouseover_colors=button_highlight_color, font=text_font, border_width=5),
            psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
        ],
        [
            psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Automatic Best Fit', key='-BUTTON_BEST_FIT-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5)
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))]
    ]
    global primary_window
    global processor
    points_x = processor.get_x_array()
    points_y = processor.get_y_array()
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(points_x, points_y, color=button_highlight_color, marker='o')
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)


def lin_reg():
    global primary_window
    indices = processor.get_polyfit_set_order(1)
    slope = indices[1]
    intercept = indices[0]
    if len(processor.get_points()) > 0:
        regression_text = "Linear Regression: " + str(round(slope, 3)) + "x + " + str(round(intercept, 3))
    else:
        regression_text = "Cannot calculate linear regression, add at least one point"
    primary_layout = [
        [
            psg.Text(text='Proiect', font=title_font, expand_x=True, justification='center',
                     text_color=layout_text_color, background_color=layout_background_color, border_width=5)
        ],
        [
            psg.Button('Add Point', key='-BUTTON_ADD_POINT-', size=button_size, button_color=button_background_color,
                       mouseover_colors=button_highlight_color, font=text_font, border_width=5),
            psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
        ],
        [
            psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
        [psg.Text(text=regression_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                  text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
    ]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(processor.get_x_array(), processor.get_y_array(), color=button_highlight_color, marker='o')
    ax.plot(processor.get_x_array(), slope * processor.get_x_array() + intercept, color='green', label='Regression Line')
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)

def run():
    popUp.welcomePopUp()
    global processor
    global primary_window
    primary_window = psg.Window('Proiect', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(processor.get_x_array(), processor.get_y_array(), color=button_highlight_color, marker='o', label='Points')
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)

    while True:
        event, values = primary_window.read()
        if event in (None, 'Exit'):
            break
        elif event == '-BUTTON_ADD_POINT-':
            popUp.addPointPopUp(processor)
        elif event == '-BUTTON_REMOVE_POINT-':
            popUp.removePointPopUp(processor)
        elif event == '-BUTTON_LINEAR_REGRESSION-':
            lin_reg()
        # elif event == '-BUTTON_CALCULATE_INTEGRAL-':
        # elif event == '-BUTTON_CALCULATE_DERIVATIVE-':
        # elif event == '-BUTTON_PREDICT_NEXT-':
        # elif event == '-BUTTON_EXTRAPOLATE_POINT-':
        # elif event == '-BUTTON_DISPLAY_DATASET-':
        # elif event == '-BUTTON_BEST_FIT-':
        #     processor.get_polyfit_optimal()
        #     updatePlot()

    primary_window.close()

if __name__ == 'main':
    run()
