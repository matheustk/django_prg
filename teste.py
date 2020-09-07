import PySimpleGUI as sg

radio_choices = ['a', 'b', 'c']
layout = [
            [sg.Text('My layout')],
            [sg.Radio(text, 1, enable_events=True, key=text) for text in radio_choices],
            [sg.Button('Read')]
         ]

window = sg.Window('Radio Button Example', layout)

class Cachorro:
    nome = 'Rex'

    def latir(self):
        print (self.nome + " au au!")

snoppy = Cachorro()

snoppy.latir()

while True:             # Event Loop
    event, values = window.Read()
    if event is None:
        break
    print(event, values)
    snoppy.latir()