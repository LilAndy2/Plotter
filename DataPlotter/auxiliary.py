import numpy as np
import PySimpleGUI as psg
from matplotlib import pyplot as plt
import PySimpleGUI as psg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
#ASPECT VARIABLES
layout_background_color = '#EBEBD3'
layout_text_color = '#5c574f'
title_font = ('Roboto', 20, 'bold')
text_font = 'Roboto'
button_background_color = '#210B2C'
button_highlight_color = '#55286F'
button_size = (10, 2)

#GLOBAL VARIABLES
global points
points = []
# points_x = [x for x,y in points]
# points_y = [y for x,y in points]
points_x = None
points_y = None

#TODO remove these at the end
points = [(1,2), (2,6) ,(1,7)]
points_x = [x for x,y in points]
points_y = [y for x,y in points]

global slope
global intercept
slope = None
intercept = None


matplotlib.use('TkAgg')
   
primary_layout = [
        [
        psg.Text(text='Proiect',font= title_font,expand_x=True,justification='center',text_color=layout_text_color,background_color=layout_background_color)
        ],
        [
        psg.Button('Add Point', key='-BUTTON_ADD_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-' , size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        ],
        [
        psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))]
    ]







def draw_figure(canvas, figure):
   tkcanvas = FigureCanvasTkAgg(figure, canvas)
   tkcanvas.draw()
   tkcanvas.get_tk_widget().pack(side='top', fill='both', expand=1)
   return tkcanvas


def addPointPopUp_from_button():
    layout = [
        [psg.Text('X ', size=(10, 1), font = text_font, text_color= layout_text_color, background_color=layout_background_color, justification= 'center'), psg.Input(expand_x=True)],
        [psg.Text('Y ', size=(10, 1), font = text_font,text_color= layout_text_color, background_color=layout_background_color, justification= 'center'), psg.Input(expand_x=True)],
        [psg.OK(button_color= button_background_color, font = text_font), 
         psg.Cancel(button_color= button_background_color, font = text_font)]
    ]
    popup_window = psg.Window('Add', layout, size=(200, 200), background_color=layout_background_color)
    event, values = popup_window.read()

    if event == 'OK':
        x, y = float(values[0]), float(values[1])
        points.append((x,y))
        print(points)
        # Actualizați și afișați graficul în timp real în fereastra principală
        updatePlot()

        popup_window.close()

    return None

def removePointPopUp_from_button():
    layout = [
        [psg.Text('X ', size=(10, 1), font = text_font, text_color= layout_text_color, background_color=layout_background_color, justification= 'center'), psg.Input(expand_x=True)],
        [psg.Text('Y ', size=(10, 1), font = text_font,text_color= layout_text_color, background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.OK(button_color= button_background_color, font = text_font), psg.Cancel(button_color= button_background_color, font = text_font)]
    ]
    popup_window = psg.Window('Remove', layout, size=(200, 200), background_color=layout_background_color)
    event, values = popup_window.read()

    if event == 'OK':
        x, y = float(values[0]), float(values[1])
        if (x,y) in points:
            points.remove((x,y))
        # Actualizați și afișați graficul în timp real în fereastra principală
        updatePlot()

        popup_window.close()

    return None



def updatePlot():
    primary_layout = [
        [
        psg.Text(text='Proiect',font= title_font,expand_x=True,justification='center',text_color=layout_text_color,background_color=layout_background_color,border_width= 5)
        ],
        [
        psg.Button('Add Point', key='-BUTTON_ADD_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-' , size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        ],
        [
        psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))]
    ]
    global primary_window
    global points
    points_x = [x for x,y in points]
    points_y = [y for x,y in points]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(700, 700), element_justification='center', background_color=layout_background_color, location=(0,0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(points_x, points_y, color = button_highlight_color, marker='o')
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig) 

def linear_regression():
    global slope
    global primary_window
    global intercept
    global points
    points_x = [x for x,y in points]
    points_y = [y for x,y in points]
    points_x = np.array(points_x)
    points_y = np.array(points_y)
    try:
        slope, intercept = np.polyfit(points_x, points_y, 1)
    except:
        pass
    
    if len(points) > 0:
        regression_text = "Linear Regression: " +str(round(slope, 3)) + "x + " + str(round(intercept, 3))
    else:
        regression_text = "Cannot calculate linear regression, add at least one point"
    primary_layout = [
        [
        psg.Text(text='Proiect',font= title_font,expand_x=True,justification='center',text_color=layout_text_color,background_color=layout_background_color, border_width= 5)
        ],
        [
        psg.Button('Add Point', key='-BUTTON_ADD_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-' , size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        ],
        [
        psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
        [psg.Text(text=regression_text,auto_size_text= True, size=(100, 1), justification='center', font=text_font, text_color=layout_text_color, background_color=layout_background_color, border_width= 5)]
        ]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(700, 700), element_justification='center', background_color=layout_background_color, location=(0,0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(points_x, points_y, color = button_highlight_color, marker='o')
    ax.plot(points_x, slope * points_x + intercept, color = 'green', label = 'Regression Line')
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig) 

def calculate_integral():
    global slope
    global primary_window
    global intercept
    global points
    regression_line = None
    points_x = [x for x,y in points]
    points_y = [y for x,y in points]
    points_x = np.array(points_x)
    points_y = np.array(points_y)
    try:
        slope, intercept = np.polyfit(points_x, points_y, 1)
        regression_line = slope * points_x + intercept
    except:
        pass
    
    layout = [
        [psg.Text('Limita inferioara', size=(10, 1), font = text_font, text_color= layout_text_color, background_color=layout_background_color, justification= 'center'), psg.Input(expand_x=True)],
        [psg.Text('Limita superioara', size=(10, 1), font = text_font,text_color= layout_text_color, background_color=layout_background_color, justification='center'), psg.Input(expand_x=True)],
        [psg.OK(button_color= button_background_color, font = text_font), psg.Cancel(button_color= button_background_color, font = text_font)]
    ]
    popup_window = psg.Window('Limita', layout, size=(200, 200), background_color=layout_background_color)
    event, values = popup_window.read()

    if event == 'OK':
        lower_limit, upper_limit = float(values[0]), float(values[1])
    elif event == 'Cancel':
        return None
    popup_window.close()
    
    try:
        integral_value = (slope * upper_limit ** 2 / 2 + intercept * upper_limit) - (slope * lower_limit ** 2 / 2 + intercept * lower_limit)
    except:
        integral_value = None


    if integral_value != None:
        integral_text = "Integral: " +str(round(integral_value, 3))
    else:
        integral_text = "Cannot calculate integral, add at least one point"  
          
    primary_layout = [
        [
        psg.Text(text='Proiect',font= title_font,expand_x=True,justification='center',text_color=layout_text_color,background_color=layout_background_color, border_width= 5)
        ],
        [
        psg.Button('Add Point', key='-BUTTON_ADD_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-' , size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        ],
        [
        psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
        [psg.Text(text=integral_text,auto_size_text= True, size=(100, 1), justification='center', font=text_font, text_color=layout_text_color, background_color=layout_background_color, border_width= 5)]
        ]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(700, 700), element_justification='center', background_color=layout_background_color, location=(0,0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(points_x, points_y, color = button_highlight_color, marker='o')
    ax.plot(points_x, slope * points_x + intercept, color = 'green', label = 'Regression Line', )
    

    
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig)        
    
def calculate_derivative():
    global slope
    global primary_window
    global intercept
    global points
    points_x = [x for x,y in points]
    points_y = [y for x,y in points]
    points_x = np.array(points_x)
    points_y = np.array(points_y)
    try:
        slope, intercept = np.polyfit(points_x, points_y, 1)
    except:
        pass
    
    if len(points) > 0:
        derivative_text = "Derivative: " +str(round(slope, 3))
    else:
        derivative_text = "Cannot calculate derivative, add at least one point"
    primary_layout = [
        [
        psg.Text(text='Proiect',font= title_font,expand_x=True,justification='center',text_color=layout_text_color,background_color=layout_background_color, border_width= 5)
        ],
        [
        psg.Button('Add Point', key='-BUTTON_ADD_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-' , size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        ],
        [
        psg.Button('Predicted Point', key='-BUTTON_PREDICT_NEXT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-' ,size=button_size, button_color= button_background_color, mouseover_colors= button_highlight_color, font = text_font, border_width= 5),
        ],
        [psg.Canvas(key='-CANVAS-', background_color='#ffffff', size=(500, 500))],
        [psg.Text(text=derivative_text,auto_size_text= True, size=(100, 1), justification='center', font=text_font, text_color=layout_text_color, background_color=layout_background_color, border_width= 5)]
        ]
    primary_window.close()
    primary_window = psg.Window('Plotting', primary_layout, size=(700, 700), element_justification='center', background_color=layout_background_color, location=(0,0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(points_x, points_y, color = button_highlight_color, marker='o')
    ax.plot(points_x, slope * points_x + intercept, color = 'green', label = 'Regression Line')
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig) 
    
    
def extrapolate_point():
    pass

def display_dataset():
    pass
    

def predict_next():
    pass



def runner(): 
    global primary_window
    primary_window = psg.Window('Proiect', primary_layout, size=(700, 700), element_justification='center', background_color=layout_background_color, location=(0,0), finalize=True)
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(points_x, points_y, color = button_highlight_color,marker='o', label = 'Points')
    tkcanvas = draw_figure(primary_window['-CANVAS-'].TKCanvas, fig) 
    
    while True:
        event,values = primary_window.read()
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
    



if __name__ == '_main_':
    runner()