from Back.buscaTarefasExecutadas import buscadorTarefas as bt
from GUI import TelaPrincipal as telaInicio
from GUI import DownloadManager as download
from Back.BuscarAmbientes import BuscarAmbientes
import tkinter as tk
import openpyxl
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from time import sleep
from datetime import datetime


def tudo():
    # Criar a janela principal
    # janela_principal = tk.Tk()
    # aplicacao = telaInicio(janela_principal)
    # janela_principal.mainloop()
    
    
    #################### PRECISA SUBSTITUIR POR UM GET DE JSON
    dia = aplicacao.data_inicial
    # lista = aplicacao.arquivo_selecionado
    usuario = aplicacao.usuario
    senha = aplicacao.senha
    meses_atras = aplicacao.meses
    aba = aplicacao.aba

    busca = BuscarAmbientes(aba)
    listaAmbientes = busca.buscaAmbientes()
    mes_tarefas = datetime.now().month - meses_atras

    # dia = 28
    # lista = "C:\\Users\\Evne\\Documents\\ambientesCompleto.xlsx"
    # usuario = "master"
    # senha = "SNNX917"
    # meses_atras = 2

    listaTarefas=[]
    
    #Deixa a pagina invisivel
    # opcoes.add_argument('--haedless')
    
    opcoes = Options()
    opcoes.add_argument("window-size=full")
    navegador = webdriver.Edge(options=opcoes)

    # try:
    #     wb = openpyxl.load_workbook(lista)
    #     sheet = wb.active
        
    #     for x in sheet:
    #         if (x[0].value!=" ") & (x[0].value!=None):
    #             listaAmbientes.append(x[0].value)
    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")

    #cria o objeto que busca as tarefas e passa quantos meses atras e tambem o dia final do mês
    tarefas = bt(navegador,10,int(dia),int(meses_atras))
    
    try: 
        for x in listaAmbientes:
            if x[0] == "":
                listaTarefas.append([x[0],"-"])
                continue
                
            tarefas.entrarPagina(f"https://{x[0]}.umov.me/CenterWeb/")
            if not tarefas.logar(f'{usuario}',f'{senha}'):
                print(f"Não foi possivel acessar o ambiente {x[0]}, senha, login ou nome do ambiente incorretos")
                listaTarefas.append([x[0],"Deu pau"])
                continue
            sleep(1)
            tarefas.entraTarefas(f"https://{x[0]}.umov.me/CenterWeb/")
            sleep(1)
            #passar o ultimo dia do mês 
            tarefas.buscaDados()

            sleep(2)
            valor = tarefas.contarRegistros()
            listaTarefas.append([x[0],valor])
            print(f"{x[0]}: {valor}")

        navegador.close()
    except Exception as e:
        navegador.close()
        listaTarefas.append([f"Error occurred: {str(e)}"])
        #Abre a janela de download e baixa o arquivo
        janela_download = tk.Tk()
        download(janela_download,listaTarefas)
        janela_download.mainloop()
    finally:
        #Abre a janela de download e baixa o arquivo
        janela_download = tk.Tk()
        download(janela_download,listaTarefas)
        janela_download.mainloop()
    
# tudo()
