
from data_processing.processorAPI import ProcessorAPI
import console.popUpManager as popUp
import PySimpleGUI as psg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ASPECT VARIABLES
layout_background_color = '#EBEBD3'
layout_text_color = '#5c574f'
title_font = ('Roboto', 20, 'bold')
text_font = 'Roboto'
button_background_color = '#210B2C'
button_highlight_color = '#55286F'
button_size = (10, 2)


# Global processor
processor = ProcessorAPI()


# Global layout for primary window
primary_layout = [
    [
        psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center', text_color=layout_text_color,
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
        psg.Button('Automatic Best Fit', key='-BUTTON_BEST_FIT-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
        psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
        psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                   button_color=button_background_color, mouseover_colors=button_highlight_color,
                   font=text_font,
                   border_width=5)
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
            psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
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
                       border_width=5),
            psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color,
                       font=text_font,
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
    indices = []
    slope = 0
    intercept = 0
    if len(processor.get_points()) > 0:
        indices = processor.get_polyfit_lin_reg()
        slope = indices[1]
        intercept = indices[0]
        regression_text = "Linear Regression: " + str(round(slope, 3)) + "x + " + str(round(intercept, 3))
    else:
        regression_text = "Cannot calculate linear regression, add at least one point"
    primary_layout = [
        [
            psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
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
                       border_width=5),
            psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color,
                       font=text_font,
                       border_width=5)
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


def best_fit():
    global primary_window
    if processor.get_points() == None:
        best_fit_text = "Cannot calculate best fit, add at least one point"
    if len(processor.get_points()) == 0:
        best_fit_text = "Cannot calculate best fit, add at least one point"
    indices = []
    order = 0
    try:
        indices = processor.get_polyfit_optimal()
        print(indices)
        order = len(indices)
    except:
        pass
    if len(processor.get_points()) > 0:
        best_fit_text = "Best fit has order " + str(order) + "."
    primary_layout = [
        [
            psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
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
                       border_width=5),
            psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color,
                       font=text_font,
                       border_width=5)
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
        [psg.Text(text=best_fit_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                  text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
    ]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(processor.get_x_array(), processor.get_y_array(), color=button_highlight_color, marker='o')
    # plot the best fit line
    x = processor.get_x_array()
    y = []
    for i in range(len(x)):
        y.append(processor.extrapolate(x[i]).y)

    ax.plot(x, y, color='green', label='Best Fit Line')

    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)


def integrate():
    global primary_window
    layout = [
        [psg.Text('Limita inferioara', size=(15, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.Text('Limita superioara', size=(15, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.Text('Precizie', size=(15, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.OK(button_color=button_background_color, font=text_font),
         psg.Cancel(button_color=button_background_color, font=text_font)]
    ]
    popup_window = psg.Window('Limita', layout, size=(300, 200), background_color=layout_background_color)
    event, values = popup_window.read()

    if event == 'OK':
        lower_limit, upper_limit, precision = float(values[0]), float(values[1]), float(values[2])
    elif event == 'Cancel':
        return None
    popup_window.close()

    try:
        integral_value = processor.integrate(lower_limit, upper_limit, precision)
    except:
        integral_value = None

    if integral_value != None:
        integral_text = "Integral: " + str(round(integral_value, 10))
    else:
        integral_text = "Cannot calculate integral, add at least one point"

    primary_layout = [
        [
            psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
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
                       border_width=5),
            psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color,
                       font=text_font,
                       border_width=5)
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
        [psg.Text(text=integral_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                  text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
    ]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    if len(processor.pointCollection.points) > 0:
        ax.scatter(processor.get_x_array(), processor.get_y_array(), color=button_highlight_color, marker='o')
        x = processor.get_x_array()
        y = []
        indices = processor.get_polyfit_optimal()
        for i in range(len(x)):
            y.append(0)
            for j in range(len(indices)):
                y[i] += indices[j] * x[i] ** j

        ax.plot(x, y, color='green', label='Best Fit Line')

    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)

def find_extrem():

    data = list(zip(processor.get_x_array(), processor.get_y_array()))
    x_values, y_values = zip(*data)
    max_value = max(y_values)
    min_value = min(y_values)

    max_points = [(x, y) for x, y in data if y == max_value]
    min_points = [(x, y) for x, y in data if y == min_value]

    extrema_text = f"Points of Maximum: {max_points}\nPoints of Minimum: {min_points}"
    psg.popup(extrema_text, title='Extrema Points')

    return max_points, min_points

def display_dataset():
    rows = list(zip(processor.get_x_array(), processor.get_y_array()))
    top_row = ['X', 'Y']
    dataset_layout = [
        [psg.Table(values=rows, headings=top_row, justification='center', background_color='white',
                   text_color=layout_text_color, auto_size_columns=False, col_widths=[5, 5])],
    ]
    dataset_window = psg.Window('Dataset', dataset_layout, size=(200, 200), background_color=layout_background_color)
    event, values = dataset_window.read()
    if event == 'Close':
        dataset_window.close()

def extrapolate():
    global primary_window
    points_x = processor.get_x_array()
    points_y = processor.get_y_array()
    layout = [
        [psg.Text('X', size=(10, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.OK(button_color=button_background_color, font=text_font),
         psg.Cancel(button_color=button_background_color, font=text_font)]
    ]
    popup_window = psg.Window('Extrapolate', layout, size=(200, 200), background_color=layout_background_color)
    event, values = popup_window.read()
    if event == 'OK':
        try:
            processor.add_point(processor.extrapolate(float(values[0])))
            points_x = processor.get_x_array()
            points_y = processor.get_y_array()
            y_text = "Extrapolated point: " + str(processor.extrapolate(float(values[0])))
        except:
            y_text = "Cannot extrapolate point, add at least one point"
        primary_layout = [
            [
                psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
                         text_color=layout_text_color, background_color=layout_background_color, border_width=5)
            ],
            [
                psg.Button('Add Point', key='-BUTTON_ADD_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
            ],
            [
                psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Automatic Best Fit', key='-BUTTON_BEST_FIT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5),
                psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5),
                psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5)
            ],
            [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
            [psg.Text(text=y_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                      text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
        ]
        primary_window.close()
        primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                    background_color=layout_background_color, location=(0, 0), finalize=True)
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        if len(processor.pointCollection.points) > 0:
            x = processor.get_x_array()
            y = []
            indices = processor.get_polyfit_indices()
            for i in range(len(x)):
                y.append(0)
                for j in range(len(indices)):
                    y[i] += indices[j] * x[i] ** j

            ax.plot(x, y, color='green', label='Best Fit Line')
            ax.scatter(points_x, points_y, color=button_highlight_color, marker='o')
            # plot the last point as a red dot
            ax.scatter(float(values[0]), processor.extrapolate(float(values[0])).y, color='red', marker='o')
        tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)
        popup_window.close()



    elif event == 'Cancel':
        popup_window.close()

def derivative():
    global primary_window
    points_x = processor.get_x_array()
    points_y = processor.get_y_array()
    layout = [
        [psg.Text('X', size=(10, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.OK(button_color=button_background_color, font=text_font),
         psg.Cancel(button_color=button_background_color, font=text_font)]
    ]
    popup_window = psg.Window('Derivative', layout, size=(200, 200), background_color=layout_background_color)
    event, values = popup_window.read()
    if event == 'OK':
        try:
            derivative = processor.differentiate(float(values[0]))
            print(derivative)
            y_text = "Derivative in point " + str(processor.extrapolate(float(values[0]))) + ": " + str(derivative)
        except:
            y_text = "Cannot calculate derivative, add at least one point"
        primary_layout = [
            [
                psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
                         text_color=layout_text_color, background_color=layout_background_color, border_width=5)
            ],
            [
                psg.Button('Add Point', key='-BUTTON_ADD_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
            ],
            [
                psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Automatic Best Fit', key='-BUTTON_BEST_FIT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5),
                psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5),
                psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5)
            ],
            [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
            [psg.Text(text=y_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                      text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
        ]
        primary_window.close()
        primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                    background_color=layout_background_color, location=(0, 0), finalize=True)
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        if len(processor.pointCollection.points) > 0:
            x = processor.get_x_array()
            y = []
            indices = processor.get_polyfit_indices()
            for i in range(len(x)):
                y.append(0)
                for j in range(len(indices)):
                    y[i] += indices[j] * x[i] ** j

            ax.plot(x, y, color='green', label='Best Fit Line')
            ax.scatter(points_x, points_y, color=button_highlight_color, marker='o')
            # plot the extrapolated point for the derivative as a red dot
            ax.scatter(float(values[0]), processor.extrapolate(float(values[0])).y, color='red', marker='o')
        tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)
        popup_window.close()



    elif event == 'Cancel':
        popup_window.close()


def predict():
    global primary_window
    points_x = processor.get_x_array()
    points_y = processor.get_y_array()
    if len(processor.pointCollection.points) > 0:
        next = processor.predict_next()
        processor.add_point(next)
        next_point_text = "Next Point: [" + str(next) + "]"
    else:
        next_point_text = "Cannot calculate next point, add at least one point"

    primary_layout = [
        [
            psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
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
                        button_color=button_background_color, mouseover_colors=button_highlight_color,
                        font=text_font,
                        border_width=5),
            psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color,
                       font=text_font,
                       border_width=5)
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

    ax.scatter(processor.get_x_array(), processor.get_y_array(), color=button_highlight_color, marker='o')
    # plot the last point as a red dot
    try:
        ax.scatter(next.x, next.y, color='red', marker='o')
    except:
        pass
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)


def run():
    popUp.welcomePopUp()
    global processor
    global primary_window
    primary_window = psg.Window('Plotit', primary_layout, size=(1000, 1000), element_justification='center',
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
        elif event == '-BUTTON_CALCULATE_INTEGRAL-':
            integrate()
        elif event == '-BUTTON_CALCULATE_DERIVATIVE-':
            derivative()
        elif event == '-BUTTON_PREDICT_NEXT-':
            predict()
        elif event == '-BUTTON_EXTRAPOLATE_POINT-':
            extrapolate()
        elif event == '-BUTTON_DISPLAY_DATASET-':
            display_dataset()
        elif event == '-BUTTON_BEST_FIT-':
            best_fit()
        elif event == '-BUTTON_FIND_EXTREM-':
            find_extrem()
        elif event == '-BUTTON_RESET-':
            processor.reset()
            updatePlot()

    primary_window.close()

if __name__ == 'main':
    run()

from data_processing.processorAPI import ProcessorAPI
import console.popUpManager as popUp
import PySimpleGUI as psg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ASPECT VARIABLES
layout_background_color = '#EBEBD3'
layout_text_color = '#5c574f'
title_font = ('Roboto', 20, 'bold')
text_font = 'Roboto'
button_background_color = '#210B2C'
button_highlight_color = '#55286F'
button_size = (10, 1)


# Global processor
processor = ProcessorAPI()


# Global layout for primary window
primary_layout = [
    [
        psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center', text_color=layout_text_color,
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
        psg.Button('Automatic Best Fit', key='-BUTTON_BEST_FIT-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
        psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
        psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                   button_color=button_background_color, mouseover_colors=button_highlight_color,
                   font=text_font,
                   border_width=5)
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
            psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
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
                       border_width=5),
            psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color,
                       font=text_font,
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
    indices = []
    slope = 0
    intercept = 0
    if len(processor.get_points()) > 0:
        indices = processor.get_polyfit_lin_reg()
        slope = indices[1]
        intercept = indices[0]
        regression_text = "Linear Regression: " + str(round(slope, 3)) + "x + " + str(round(intercept, 3))
    else:
        regression_text = "Cannot calculate linear regression, add at least one point"
    primary_layout = [
        [
            psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
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
                       border_width=5),
            psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color,
                       font=text_font,
                       border_width=5)
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


def best_fit():
    global primary_window
    if processor.get_points() == None:
        best_fit_text = "Cannot calculate best fit, add at least one point"
    if len(processor.get_points()) == 0:
        best_fit_text = "Cannot calculate best fit, add at least one point"
    indices = []
    order = 0
    try:
        indices = processor.get_polyfit_optimal()
        print(indices)
        order = len(indices)
    except:
        pass
    if len(processor.get_points()) > 0:
        best_fit_text = "Best fit has order " + str(order) + "."
    primary_layout = [
        [
            psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
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
                       border_width=5),
            psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color,
                       font=text_font,
                       border_width=5)
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
        [psg.Text(text=best_fit_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                  text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
    ]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(processor.get_x_array(), processor.get_y_array(), color=button_highlight_color, marker='o')
    # plot the best fit line
    x = processor.get_x_array()
    y = []
    for i in range(len(x)):
        y.append(processor.extrapolate(x[i]).y)

    ax.plot(x, y, color='green', label='Best Fit Line')

    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)


def integrate():
    global primary_window
    layout = [
        [psg.Text('Limita inferioara', size=(15, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.Text('Limita superioara', size=(15, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.Text('Precizie', size=(15, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.OK(button_color=button_background_color, font=text_font),
         psg.Cancel(button_color=button_background_color, font=text_font)]
    ]
    popup_window = psg.Window('Limita', layout, size=(300, 200), background_color=layout_background_color)
    event, values = popup_window.read()

    if event == 'OK':
        lower_limit, upper_limit, precision = float(values[0]), float(values[1]), float(values[2])
    elif event == 'Cancel':
        return None
    popup_window.close()

    try:
        integral_value = processor.integrate(lower_limit, upper_limit, precision)
    except:
        integral_value = None

    if integral_value != None:
        integral_text = "Integral: " + str(round(integral_value, 10))
    else:
        integral_text = "Cannot calculate integral, add at least one point"

    primary_layout = [
        [
            psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
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
                       border_width=5),
            psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color,
                       font=text_font,
                       border_width=5)
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
        [psg.Text(text=integral_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                  text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
    ]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                background_color=layout_background_color, location=(0, 0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    if len(processor.pointCollection.points) > 0:
        ax.scatter(processor.get_x_array(), processor.get_y_array(), color=button_highlight_color, marker='o')
        x = processor.get_x_array()
        y = []
        indices = processor.get_polyfit_optimal()
        for i in range(len(x)):
            y.append(0)
            for j in range(len(indices)):
                y[i] += indices[j] * x[i] ** j

        ax.plot(x, y, color='green', label='Best Fit Line')

    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)

def find_extrem():

    data = list(zip(processor.get_x_array(), processor.get_y_array()))
    x_values, y_values = zip(*data)
    max_value = max(y_values)
    min_value = min(y_values)

    max_points = [(x, y) for x, y in data if y == max_value]
    min_points = [(x, y) for x, y in data if y == min_value]

    extrema_text = f"Points of Maximum: {max_points}\nPoints of Minimum: {min_points}"
    psg.popup(extrema_text, title='Extrema Points')

    return max_points, min_points

def display_dataset():
    rows = list(zip(processor.get_x_array(), processor.get_y_array()))
    top_row = ['X', 'Y']
    dataset_layout = [
        [psg.Table(values=rows, headings=top_row, justification='center', background_color='white',
                   text_color=layout_text_color, auto_size_columns=False, col_widths=[5, 5])],
    ]
    dataset_window = psg.Window('Dataset', dataset_layout, size=(200, 200), background_color=layout_background_color)
    event, values = dataset_window.read()
    if event == 'Close':
        dataset_window.close()

def extrapolate():
    global primary_window
    points_x = processor.get_x_array()
    points_y = processor.get_y_array()
    layout = [
        [psg.Text('X', size=(10, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.OK(button_color=button_background_color, font=text_font),
         psg.Cancel(button_color=button_background_color, font=text_font)]
    ]
    popup_window = psg.Window('Extrapolate', layout, size=(200, 200), background_color=layout_background_color)
    event, values = popup_window.read()
    if event == 'OK':
        try:
            processor.add_point(processor.extrapolate(float(values[0])))
            points_x = processor.get_x_array()
            points_y = processor.get_y_array()
            y_text = "Extrapolated point: " + str(processor.extrapolate(float(values[0])))
        except:
            y_text = "Cannot extrapolate point, add at least one point"
        primary_layout = [
            [
                psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
                         text_color=layout_text_color, background_color=layout_background_color, border_width=5)
            ],
            [
                psg.Button('Add Point', key='-BUTTON_ADD_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
            ],
            [
                psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Automatic Best Fit', key='-BUTTON_BEST_FIT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5),
                psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5),
                psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5)
            ],
            [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
            [psg.Text(text=y_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                      text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
        ]
        primary_window.close()
        primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                    background_color=layout_background_color, location=(0, 0), finalize=True)
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        if len(processor.pointCollection.points) > 0:
            x = processor.get_x_array()
            y = []
            indices = processor.get_polyfit_indices()
            for i in range(len(x)):
                y.append(0)
                for j in range(len(indices)):
                    y[i] += indices[j] * x[i] ** j

            ax.plot(x, y, color='green', label='Best Fit Line')
            ax.scatter(points_x, points_y, color=button_highlight_color, marker='o')
            # plot the last point as a red dot
            ax.scatter(float(values[0]), processor.extrapolate(float(values[0])).y, color='red', marker='o')
        tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)
        popup_window.close()



    elif event == 'Cancel':
        popup_window.close()

def derivative():
    global primary_window
    points_x = processor.get_x_array()
    points_y = processor.get_y_array()
    layout = [
        [psg.Text('X', size=(10, 1), font=text_font, text_color=layout_text_color,
                  background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.OK(button_color=button_background_color, font=text_font),
         psg.Cancel(button_color=button_background_color, font=text_font)]
    ]
    popup_window = psg.Window('Derivative', layout, size=(200, 200), background_color=layout_background_color)
    event, values = popup_window.read()
    if event == 'OK':
        try:
            derivative = processor.differentiate(float(values[0]))
            print(derivative)
            y_text = "Derivative in point " + str(processor.extrapolate(float(values[0]))) + ": " + str(derivative)
        except:
            y_text = "Cannot calculate derivative, add at least one point"
        primary_layout = [
            [
                psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
                         text_color=layout_text_color, background_color=layout_background_color, border_width=5)
            ],
            [
                psg.Button('Add Point', key='-BUTTON_ADD_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
            ],
            [
                psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font, border_width=5),
                psg.Button('Automatic Best Fit', key='-BUTTON_BEST_FIT-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5),
                psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5),
                psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                           button_color=button_background_color, mouseover_colors=button_highlight_color,
                           font=text_font,
                           border_width=5)
            ],
            [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
            [psg.Text(text=y_text, auto_size_text=True, size=(100, 1), justification='center', font=text_font,
                      text_color=layout_text_color, background_color=layout_background_color, border_width=5)]
        ]
        primary_window.close()
        primary_window = psg.Window('Plotting', primary_layout, size=(1000, 1000), element_justification='center',
                                    background_color=layout_background_color, location=(0, 0), finalize=True)
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        if len(processor.pointCollection.points) > 0:
            x = processor.get_x_array()
            y = []
            indices = processor.get_polyfit_indices()
            for i in range(len(x)):
                y.append(0)
                for j in range(len(indices)):
                    y[i] += indices[j] * x[i] ** j

            ax.plot(x, y, color='green', label='Best Fit Line')
            ax.scatter(points_x, points_y, color=button_highlight_color, marker='o')
            # plot the extrapolated point for the derivative as a red dot
            ax.scatter(float(values[0]), processor.extrapolate(float(values[0])).y, color='red', marker='o')
        tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)
        popup_window.close()



    elif event == 'Cancel':
        popup_window.close()


def predict():
    global primary_window
    points_x = processor.get_x_array()
    points_y = processor.get_y_array()
    if len(processor.pointCollection.points) > 0:
        next = processor.predict_next()
        processor.add_point(next)
        next_point_text = "Next Point: [" + str(next) + "]"
    else:
        next_point_text = "Cannot calculate next point, add at least one point"

    primary_layout = [
        [
            psg.Text(text='Plotit - Your one and only data plotter', font=title_font, expand_x=True, justification='center',
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
                        button_color=button_background_color, mouseover_colors=button_highlight_color,
                        font=text_font,
                        border_width=5),
            psg.Button('Find Extrem Points', key='-BUTTON_FIND_EXTREM-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color, font=text_font,
                       border_width=5),
            psg.Button('Reset', key='-BUTTON_RESET-', size=button_size,
                       button_color=button_background_color, mouseover_colors=button_highlight_color,
                       font=text_font,
                       border_width=5)
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

    ax.scatter(processor.get_x_array(), processor.get_y_array(), color=button_highlight_color, marker='o')
    # plot the last point as a red dot
    try:
        ax.scatter(next.x, next.y, color='red', marker='o')
    except:
        pass
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)


def populate_distribution():
    # popup for normal distribution
    popUp.populateNormal(processor)

def run():
    popUp.welcomePopUp()
    global processor
    global primary_window
    primary_window = psg.Window('Plotit', primary_layout, size=(1000, 1000), element_justification='center',
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
        elif event == '-BUTTON_CALCULATE_INTEGRAL-':
            integrate()
        elif event == '-BUTTON_CALCULATE_DERIVATIVE-':
            derivative()
        elif event == '-BUTTON_PREDICT_NEXT-':
            predict()
        elif event == '-BUTTON_EXTRAPOLATE_POINT-':
            extrapolate()
        elif event == '-BUTTON_DISPLAY_DATASET-':
            display_dataset()
        elif event == '-BUTTON_BEST_FIT-':
            best_fit()
        elif event == '-BUTTON_FIND_EXTREM-':
            find_extrem()
        elif event == '-BUTTON_RESET-':
            processor.reset()
            updatePlot()

    primary_window.close()

if __name__ == 'main':
    run()

