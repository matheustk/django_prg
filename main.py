#!/usr/bin/env Python3      
import PySimpleGUI as sg      
import gui_proc as proc

#sg.ChangeLookAndFeel('GreenTan')      
#sg.theme('DarkAmber')    # Keep things interesting for your users

# ------ Menu Definition ------ #      
menu_def = [['Processo', ['Agendamentos', 'Processos', 'Scripts' , 'Exit']],   
            ['Help', 'About...'] ]      

# ------ Column Definition ------ #      
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      

layout = [      
    [sg.Menu(menu_def, tearoff=True)]]    

window = sg.Window('Principal', layout, default_element_size=(40, 1), grab_anywhere=False)      

while True:             # Event Loop

    event, values = window.read()
    if event in (None, 'Exit'):
        break

    if event == 'Processos':
        proc.main()


window.close()    

sg.popup('Title',      
            'The results of the window.',      
            'The button clicked was "{}"'.format(event),      
            'The values are', values)      