

import PySimpleGUI as sg
import json
from json import (load as jsonload, dump as jsondump)
from os import path

# Carregar base de dados para a tela.
SETTINGS_FILE = path.join(path.dirname(__file__), r'processo.dat')

DEFAULT_SETTINGS = {'nom_proc': 'Base_Unica', 'cod_proc': 1 }
# "Mapeamento" do arquivo de dados para as chaves da inteface
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'nom_proc': '-NOM_PROC-', 'cod_proc': '-COD_PROC-'}

##################### Load/Save Settings File #####################
def load_settings(settings_file, default_settings):
    settingsList = []
    try:        
        print("Started Reading JSON file which contains multiple JSON document")
        with open(settings_file, 'r') as f:
            for jsonObj in f:
                settingsList = json.loads(jsonObj)



    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settingsList.append(default_settings)
        save_settings(settings_file, settingsList, None)
    return settingsList


def save_settings(settings_file, settingsList, values):
    settingsDict = {'nom_proc': 'Base_Unica', 'cod_proc': 1 }
    if values:      # if there are stuff specified by another window, fill in those values
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
            try:
                settingsDict[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')
        settingsList.append(settingsDict)

    with open(settings_file, 'w') as f:
        jsondump(settingsList, f)

    sg.popup('Settings saved')

##################### Make a settings window #####################
def create_window(settings):
    #sg.theme('')

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Processos', font='Any 15')],
                [TextLabel('Código do Processo'), sg.Input(key='-COD_PROC-')],
                [TextLabel('Nome Processo'),sg.Input(key='-NOM_PROC-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:   # carregar dados dos campos com o último cadastro
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window

##################### Main Program Window & Event Loop #####################
def create_main_window(settingsList):
    #sg.theme(settings['theme'])

    layout = [[sg.T('This is my main application')],
              [sg.T('Add your primary window stuff in here')]]
    
    for x in range(len(settingsList)):
        layout.append([sg.Radio(text=settingsList[x]["cod_proc"] + ' : ' + settingsList[x]["nom_proc"], group_id = 'id_proc', key=x, enable_events=True)])
    
    layout.append([sg.B('Ok'), sg.B('Exit'), sg.B('Change Settings')])

    return sg.Window('Main Application', layout)


def main():
    window, settingsList = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    rb = '0'
    while True:             # Event Loop
        if window is None:
            window = create_main_window(settingsList)

        event, values = window.read()
        if event in (None, 'Exit'):
            break

        elif event == 'Change Settings':

            event, values = create_window(settingsList[rb]).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settingsList, values)
        
        else:
            rb = event
    window.close()
#main()