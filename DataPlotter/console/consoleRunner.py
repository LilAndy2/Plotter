import PySimpleGUI as psg


def runner():
    layout = [[psg.Text(text='Hello World',
                        font=('Arial Bold', 20),
                        size=20,
                        expand_x=True,
                        justification='center')],
              ]
    window = psg.Window('HelloWorld', layout, size=(700, 700))
    file = open("utils/OpenPopUpText.txt", "r")
    text = file.read()
    psg.popup_scrolled(text, title="Scrolled Popup", font=("Arial Bold", 16), size=(70, 10))
    while True:
        event, values = window.read()
        print(event, values)
        if event in (None, 'Exit'):
            break
    window.close()
