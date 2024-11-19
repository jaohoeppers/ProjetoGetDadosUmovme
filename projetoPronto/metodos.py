from buscaTarefasExecutadas import buscadorTarefas as bt
from GUI import TelaPrincipal as telaInicio
from GUI import DownloadManager as download
import tkinter as tk
import openpyxl
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from time import sleep


def tudo():
    # Criar a janela principal
    janela_principal = tk.Tk()
    aplicacao = telaInicio(janela_principal)
    janela_principal.mainloop()

    dia = aplicacao.data_inicial
    lista = aplicacao.arquivo_selecionado
    listaAmbientes=[]
    listaTarefas=[]

    
    #Deixa a pagina invisivel
    # opcoes.add_argument('--haedless')
    opcoes = Options()
    opcoes.add_argument('window-size=1366,900')
    navegador = webdriver.Edge(options=opcoes)

    try:
        wb = openpyxl.load_workbook(lista)
        sheet = wb.active
        
        for x in sheet:
            if (x[0].value!='') & (x[0].value!=None):
                listaAmbientes.append(x[0].value)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    tarefas = bt(navegador,10,int(dia))

    for x in listaAmbientes:
        tarefas.entrarPagina(f"https://{x}.umov.me/CenterWeb/")
        if not tarefas.logar('master','SNNX917'):
            print(f'Não foi possivel acessar o ambiente {x}, senha ou login incorretos')
            continue
        tarefas.entraTarefas(f"https://{x}.umov.me/CenterWeb/")

        #passar o ultimo dia do mês 
        tarefas.buscaDados()

        sleep(2)
        valor = tarefas.contarRegistros()
        listaTarefas.append([x,valor])
        print(f"{x}: {valor}")

    navegador.close()

    #Abre a janela de download e baixa o arquivo
    janela_download = tk.Tk()
    aplicacao = download(janela_download,listaTarefas)

    janela_download.mainloop()
    
tudo()
