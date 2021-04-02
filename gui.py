import PySimpleGUI as sg
import main

layout = [[sg.Text("Path: ")],
          [sg.Input(key='-INPUT-PATH-')],
          [sg.Text("Regular Expression: ")],
          [sg.Input(key='-INPUT-RE-')],
          [sg.Listbox(values=[], size=(40, 1), key="-FILE LIST-")],
          [sg.Button('Ok'), sg.Button('Quit')]]
window = sg.Window('File Searcher by Estefania Jimenez-A01635062', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    fileList = main.getRE(str(values['-INPUT-RE-']), str(values['-INPUT-PATH-']))
    window["-FILE LIST-"].update(fileList)
window.close()