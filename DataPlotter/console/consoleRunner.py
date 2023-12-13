import PySimpleGUI as psg

def runner():
    layout = [[psg.Text("Hello from PySimpleGUI")], [psg.Button("OK")]]
    window = psg.Window("Demo", layout)
    while True:
        event, values = window.read()
        if event == "OK" or event == psg.WIN_CLOSED:
            break
    window.close()