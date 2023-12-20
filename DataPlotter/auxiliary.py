import numpy as np
import PySimpleGUI as psg
from matplotlib import pyplot as plt
import PySimpleGUI as psg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import sklearn.linear_model as LinearRegression

# ASPECT VARIABLES
layout_background_color = '#EBEBD3'
layout_text_color = '#5c574f'
title_font = ('Roboto', 20, 'bold')
text_font = 'Roboto'
button_background_color = '#210B2C'
button_highlight_color = '#55286F'
button_size = (10, 2)

# GLOBAL VARIABLES
global points
points = []
# points_x = [x for x,y in points]
# points_y = [y for x,y in points]
points_x = None
points_y = None

# TODO remove these at the end
# points = [(1,2), (2,6) ,(1,7), (5,11)]
# points_x = [x for x,y in points]
# points_y = [y for x,y in points]

global slope
global intercept
slope = None
intercept = None

matplotlib.use('TkAgg')

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
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))]
    ]
    global primary_window
    global points
    points_x = [x for x, y in points]
    points_y = [y for x, y in points]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(points_x, points_y, color=button_highlight_color, marker='o')
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)


def calculate_derivative():
    global slope
    global primary_window
    global intercept
    global points
    points_x = [x for x, y in points]
    points_y = [y for x, y in points]
    points_x = np.array(points_x)
    points_y = np.array(points_y)
    try:
        slope, intercept = np.polyfit(points_x, points_y, 1)
    except:
        pass

    if len(points) > 0:
        derivative_text = "Derivative: " + str(round(slope, 3))
    else:
        derivative_text = "Cannot calculate derivative, add at least one point"
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
        [psg.Text(text=derivative_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                  text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
    ]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(points_x, points_y, color=button_highlight_color, marker='o')
    ax.plot(points_x, slope * points_x + intercept, color='green', label='Regression Line')
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)


def predict_next():
    global points
    global primary_window
    points_x = [x for x, y in points]
    points_y = [y for x, y in points]

    if len(points) > 0:
        X = np.arange(1, len(points) + 1).reshape(-1, 1)
        y = np.array(points)
        model = LinearRegression.LinearRegression()
        model.fit(X, y)
        next_index = len(points) + 1
        next_point = model.predict([[next_index]])
        print(next_point)
        points.append((next_point[0][0], next_point[0][1]))
        points_x = [x for x, y in points]
        points_y = [y for x, y in points]
        next_point_text = "Next Point: [" + str(next_point[0][0]) + ", " + str(next_point[0][1]) + "]"
    else:
        next_point_text = "Cannot calculate next point, add at least one point"

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
        [psg.Text(text=next_point_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                  text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
    ]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    ax.scatter(points_x, points_y, color=button_highlight_color, marker='o')
    # plot the last point as a red dot
    try:
        ax.scatter(next_point[0][0], next_point[0][1], color='red', marker='o')
    except:
        pass
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)


def runner():
    global primary_window
    primary_window = psg.Window('Proiect', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(points_x, points_y, color=button_highlight_color, marker='o', label='Points')
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)

    while True:
        event, values = primary_window.read()
        if event in (None, 'Exit'):
            break
        elif event == '-BUTTON_ADD_POINT-':
            addPointPopUp_from_button()
        elif event == '-BUTTON_REMOVE_POINT-':
            removePointPopUp_from_button()
        elif event == '-BUTTON_LINEAR_REGRESSION-':
            linear_regression()
        elif event == '-BUTTON_CALCULATE_INTEGRAL-':
            calculate_integral()
        elif event == '-BUTTON_CALCULATE_DERIVATIVE-':
            calculate_derivative()
        elif event == '-BUTTON_PREDICT_NEXT-':
            predict_next()
        elif event == '-BUTTON_EXTRAPOLATE_POINT-':
            extrapolate_point()
        elif event == '-BUTTON_DISPLAY_DATASET-':
            display_dataset()

    primary_window.close()


if __name__ == 'main':
    runner()
