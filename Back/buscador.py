from Back.buscaTarefasExecutadas import buscadorTarefas as bt
# from GUI import TelaPrincipal as telaInicio
from GUI import DownloadManager as download
from Back.BuscarAmbientes import BuscarAmbientes
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from time import sleep
from datetime import datetime

class buscador:
    def __init__(self, json_data):
        dia = json_data['dia']
        self.usuario = json_data['usuario']
        self.senha = json_data['senha']
        meses_atras = json_data['meses_atras']
        aba = json_data['aba']
        self.listaTarefas = []
        
        ############################
        ###VARIAVEIS PARA TESTE
        # self.dia = 28
        self.lista = "C:\\Users\\Evne\\Documents\\ambientesCompleto.xlsx"
        # self.usuario = "master"
        # self.senha = "SNNX917"
        # self.meses_atras = 2
        ############################
        
        self.mes_tarefas = datetime.now().month - meses_atras
        # self.listaAmbientes = BuscarAmbientes(aba).buscaAmbientes()
        
        #VARIAVEIS DO NAVEGADOR
        opcoes = Options()
        opcoes.add_argument("window-size=full")
        #Deixa a pagina invisivel
        # opcoes.add_argument('--haedless')
        self.navegador = webdriver.Edge(options=opcoes) 
        #cria o objeto que busca as tarefas e passa quantos meses atras e tambem o dia final do mês
        self.tarefas = bt(self.navegador,10,int(dia),int(meses_atras))
        
        


    def loopPrincipal(self):
        
        try: 
            for x in self.listaAmbientes:
                if x[0] == "":
                    self.listaTarefas.append([x[0],"-"])
                    continue
                    
                self.tarefas.entrarPagina(f"https://{x[0]}.umov.me/CenterWeb/")
                if not self.tarefas.logar(f'{self.usuario}',f'{self.senha}'):
                    print(f"Não foi possivel acessar o ambiente {x[0]}, senha, login ou nome do ambiente incorretos")
                    self.listaTarefas.append([x[0],"Deu pau"])
                    continue
                sleep(1)
                self.tarefas.entraTarefas(f"https://{x[0]}.umov.me/CenterWeb/")
                sleep(1)
                #passar o ultimo dia do mês 
                self.tarefas.buscaDados()

                sleep(2)
                valor = self.tarefas.contarRegistros()
                self.listaTarefas.append([x[0],valor])
                print(f"{x[0]}: {valor}")

            self.navegador.close()
        except Exception as e:
            self.salvarPosErro(e)
        finally:
            self.salvarTarefas
            
    def salvarPosErro(self, e):
        self.navegador.close()
        self.listaTarefas.append([f"Error occurred: {str(e)}"])
        self.salvarTarefas()
        
    def salvarTarefas(self):
        #Abre a janela de download e baixa o arquivo
        janela_download = tk.Tk()
        download(janela_download,self.listaTarefas)
        janela_download.mainloop()
        
    # tudo()
