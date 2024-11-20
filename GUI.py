import tkinter as tk
from tkinter import filedialog
import pandas as pd

class TelaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Seleção de Arquivo")
        
        # Botão para abrir a seleção de arquivo
        self.mensagem = tk.Label(self.master,text="ESTE SISTEMA FUNCIONA APENAS PARA COLETA DE TAREFAS EXECUTADAS NO MÊS ANTERIOR AO ATUAL").pack()
        self.selecionar_arquivo_button = tk.Button(self.master, text="Iniciar coleta de tarefas executadas", command=self.abrir_selecao_arquivo)
        self.selecionar_arquivo_button.pack(pady=10)
        
        # Variáveis para armazenar os dados
        self.data_inicial = None
        self.arquivo_selecionado = None
        # self.master.destroy()

    def abrir_selecao_arquivo(self):
        # Abrir a janela de seleção de arquivo
        self.janela_selecao = tk.Toplevel(self.master)
        self.janela_selecao.title("Selecione o Arquivo")
        
        # Campo para inserir o valor inteiro
        tk.Label(self.janela_selecao, text="Selecione o ultimo dia do mês anterior").pack()
        self.data_inicial_entry = tk.Entry(self.janela_selecao)
        self.data_inicial_entry.pack()
        
        # Botão para confirmar a seleção
        confirmar_button = tk.Button(self.janela_selecao, text="Confirmar", command=self.confirmar_selecao)
        confirmar_button.pack(pady=10)
        
        # Botão para cancelar a seleção
        cancelar_button = tk.Button(self.janela_selecao, text="Cancelar", command=self.janela_selecao.destroy)
        cancelar_button.pack()

    def confirmar_selecao(self):
        # Obter o valor da data inicial
        try:
            self.data_inicial = int(self.data_inicial_entry.get())
            
            # Selecionar o arquivo
            self.arquivo_selecionado = filedialog.askopenfilename(title="Selecione o Arquivo")
            
            # Fechar a janela de seleção
            self.janela_selecao.destroy()
            
            # Imprimir os dados coletados
            print(f"Data Inicial: {self.data_inicial}")
            print(f"Arquivo Selecionado: {self.arquivo_selecionado}")
            self.master.destroy()
        except ValueError:
            print("Por favor, insira um valor inteiro válido para Data Inicial.")

#**************************************************************************************************************

class DownloadManager:
    def __init__(self, master,arquivo):
        self.master1 = master
        self.master1.title("Gerenciador de Downloads")

        self.arquivo = arquivo
        
        # Botão para selecionar a pasta de destino
        self.selecionar_pasta_button = tk.Button(self.master1, text="Selecione a Pasta", command=self.selecionar_pasta)
        self.selecionar_pasta_button.pack(pady=10)
        
        # Label para exibir o caminho da pasta selecionada
        self.caminho_pasta_label = tk.Label(self.master1, text="Caminho da Pasta:")
        self.caminho_pasta_label.pack()
        
        # Botão para iniciar o download
        self.iniciar_download_button = tk.Button(self.master1, text="Iniciar Download", command=self.iniciar_download)
        self.iniciar_download_button.pack(pady=10)

        # self.master1.destroy()

    def selecionar_pasta(self):
        try:
            # Abrir a janela para selecionar a pasta
            self.caminho_pasta = filedialog.askdirectory(title="Selecione a Pasta de Destino")
            
            # Verificar se uma pasta foi selecionada
            if self.caminho_pasta:
                self.caminho_pasta_label.config(text=f"Caminho Selecionado: {self.caminho_pasta}")
            else:
                print("Nenhuma pasta selecionada.")
        except Exception as e:
            print(f"Erro ao selecionar pasta: {str(e)}")

    def iniciar_download(self):
        pd.DataFrame(self.arquivo, columns=("Ambiente", "tarefas")).to_excel(f'{self.caminho_pasta}/tarefas.xlsx', index=False)
        self.limpar_tela()
        self.mostrarConcluido()
        # self.master1.destroy()

    def limpar_tela(self):
        for widget in self.master1.winfo_children():
            widget.destroy()

    def mostrarConcluido(self):
        # self.master1.clear()
        self.master1.title("CONCLUIDO")
        texto = tk.Label(self.master1, text="DOWNLOAD CONCLUIDO COM SUCESSO").pack()
