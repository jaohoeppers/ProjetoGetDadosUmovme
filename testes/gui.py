import PySimpleGUI as sg
import pandas as pd

def create_gui():
    layout = [
        [
            sg.Text('Digite o ultimo dia do mes anterior'),
            sg.Input(key = 'dia'),
            sg.Text("Selecione o arquivo com os ambientes"), 
            sg.Input(key="arquivo"), 
            sg.FileBrowse(file_types=(("All Files", "*.*"),("Excel Files", "*.xlsx"))),
            sg.Button("ENVIAR")
        ]
    ]

    window = sg.Window("File Selector", layout)

    while True:
        evento, valores = window.read()
        if evento == sg.WINDOW_CLOSED:
            break
        elif evento == "ENVIAR":
            diaFinal = valores["dia"]
            arquivo = valores['arquivo']
            window.close()    
            return(diaFinal,arquivo)
    window.close() 

def baixar(arquivo):
    layout = [[
        sg.Text('Baixar o Arquivo'),
        sg.Button('DOWNLOAD'),
        sg.Text("Selecione a pasta para baixar o arquivo"), 
        sg.Input(key="Caminho"), 
        sg.FolderBrowse(key="pasta")]
    ]
    window = sg.Window("Baixar", layout)
    
    evento,valores = window.read()
    x=valores['pasta']
    if evento == 'DOWNLOAD':
        print(valores)
        pd.DataFrame(arquivo, columns=("Ambiente", "tarefas")).to_excel(f'{x}/tarefas.xlsx', index=False)
        window.close()

# create_gui()






# import PySimpleGUI as sg

# # layout = [[sg.Text("Digite seu nome:")], [sg.Input()], [sg.Button("Enviar")]]
# layout=[
#     sg.Text("Select a file:"), 
#     sg.Input(key="-FILE-"), 
#     sg.FileBrowse(file_types=(("All Files", "*.*"), ("Text Files", "*.txt;*.csv"), ("Excel Files", "*.xlsx"))),
#     sg.Button("Open")
#     ]
# window = sg.Window("Meu App", layout)

# print(window.read())

# # while True:
# #     event, values = window.read()
# #     if event == sg.WIN_CLOSED:
# #         break
# #     elif event == "Enviar":
# #         print(f"Olá, {values[0]}!")
# #         break

# window.close()
