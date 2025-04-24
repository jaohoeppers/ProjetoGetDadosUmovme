import tkinter as tk
from tkinter import filedialog
import pandas as pd

class TelaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Coletor de Tarefas Executadas")
        
        # Botão para abrir a seleção de arquivo
        self.mensagem = tk.Label(self.master,text="ESTE SISTEMA FUNCIONA APENAS PARA COLETA DE TAREFAS EXECUTADAS NO MÊS ANTERIOR AO ATUAL").pack()
        self.selecionar_arquivo_button = tk.Button(self.master, text="Iniciar coleta de tarefas executadas", command=self.selecao_meses_diames)
        self.selecionar_arquivo_button.pack(pady=10)
        
        # Variáveis para armazenar os dados principais
        self.data_inicial = None
        self.arquivo_selecionado = None
        self.usuario = None
        self.senha = None
        self.meses = None
        self.aba = None

        #Variáveis para armazenar os dados dos widgets
        # self.meses_entry = None
        # self.data_inicial_entry = None
        # self.usuario_entry = None
        # self.senha_entry = None
        # self.master.destroy()

    def selecao_meses_diames(self):
        # Abrir a janela
        self.janela_selecao_datas = tk.Toplevel(self.master)
        self.janela_selecao_datas.title("Selecione o dia")

        # Campo para inserir quantidade de meses atras
        tk.Label(self.janela_selecao_datas, text="Selecione o numero de meses anteriores").pack()
        tk.Label(self.janela_selecao_datas, text="EX: Se estamos no mes de outubro e você quer pegar as tarefas do mes de julho voce precisa digitar 3",bg="blue",fg="white").pack()
        self.meses_entry = tk.Entry(self.janela_selecao_datas)
        self.meses_entry.pack()
        # self.meses=self.meses_entry.get()
        
        # Campo para inserir o ultimo dia do mes escolhido
        tk.Label(self.janela_selecao_datas, text="Selecione o ultimo dia do mês escolhido").pack()
        self.data_inicial_entry = tk.Entry(self.janela_selecao_datas)
        self.data_inicial_entry.pack()
        # self.data_inicial=self.data_inicial_entry.get()
        
        # Botão para confirmar a seleção
        confirmar_button = tk.Button(self.janela_selecao_datas, text="Confirmar", command=self.abrir_selecao_usuariosenha)
        confirmar_button.pack(pady=10)
        
        # Botão para cancelar a seleção
        cancelar_button = tk.Button(self.janela_selecao_datas, text="Cancelar", command=self.janela_selecao_datas.destroy)
        cancelar_button.pack()

    def abrir_selecao_usuariosenha(self):
        
        # Abrir a janela
        self.janela_selecao_usuario_senha = tk.Toplevel(self.master)
        self.janela_selecao_usuario_senha.title("Seleção Usuario e Senha")

        # self.janela_selecao_datas.destroy()

        # Campo para inserir o nome do usuario
        tk.Label(self.janela_selecao_usuario_senha, text="Digite o Usuario").pack()
        self.usuario_entry = tk.Entry(self.janela_selecao_usuario_senha)
        self.usuario_entry.pack()

        # Campo para inserir a senha
        tk.Label(self.janela_selecao_usuario_senha, text="Digite a Senha dos Ambientes").pack()
        self.senha_entry = tk.Entry(self.janela_selecao_usuario_senha)
        self.senha_entry.pack()
        
        tk.Label(self.janela_selecao_usuario_senha, text="Digite a Aba da Planilha").pack()
        self.aba_entry = tk.Entry(self.janela_selecao_usuario_senha)
        self.aba_entry.pack()
        
        # Botão para confirmar
        # confirmar_button = tk.Button(self.janela_selecao_usuario_senha, text="Confirmar", command=self.abrir_selecao_arquivo)
        confirmar_button = tk.Button(self.janela_selecao_usuario_senha, text="Confirmar", command=self.confirmar_selecao)
        confirmar_button.pack(pady=10)
        
        # Botão para cancelar
        cancelar_button = tk.Button(self.janela_selecao_usuario_senha, text="Cancelar", command=self.janela_selecao_usuario_senha.destroy)
        cancelar_button.pack()
    
    # def abrir_selecao_arquivo(self):
    #     self.janela_selecao_arquivo = tk.Toplevel(self.master)
    #     self.janela_selecao_arquivo.title("Arquivo")

    #     # self.janela_selecao_usuario_senha.destroy()
        
    #     # Campo para inserir o nome do usuario
    #     self.arquivo =tk.Label(self.janela_selecao_arquivo, text="Arquivo").pack()

    #     self.escolher_button = tk.Button(self.janela_selecao_arquivo, text="Escolher Arquivo", command=self.selecionar_arquivo).pack(pady=10)

    #     self.Finalizar = tk.Button(self.janela_selecao_arquivo, text="INICIAR", command=self.confirmar_selecao,bg='black',fg='white').pack(pady=10)

    def selecionar_arquivo(self):

        # try:
        # Abrir a janela para selecionar a o arquivo
        self.arquivo_selecionado = filedialog.askopenfilename(title="Selecione o Arquivo")
        # self.finalizar = self.confirmar_selecao
        
        # Verificar se um arquivo foi selecionado
        # if self.arquivo_selecionado:
        #     self.arquivo.config(text=f"Caminho Selecionado: {self.arquivo_selecionado}")
        # else:
        #     print("Nenhuma pasta selecionada.")
        # except Exception as e:
        #     print(f"Erro ao selecionar arquivo: {str(e)}")

    def confirmar_selecao(self):

        # Obter o valor da data inicial
        try:
            self.data_inicial = int(self.data_inicial_entry.get())
            self.meses = int(self.meses_entry.get())
            self.usuario = (self.usuario_entry.get())
            self.senha = (self.senha_entry.get())   
            self.aba = (self.aba_entry.get())           
            
            # Fechar a janela de seleção
            self.janela_selecao_usuario_senha.destroy()
            
            # Imprimir os dados coletados
            print(f"Meses atras: {self.meses}")
            print(f"Data Final: {self.data_inicial}")
            print(f"Usuario: {self.usuario}")
            print(f"Senha: {self.senha}")
            print(f"Aba Planilha: {self.senha}")
            print('---------------------------------')
            self.master.destroy()
        except ValueError:
            print("Por favor, insira um valor inteiro válido para Data Inicial ou meses anteriores.")

#**************************************************************************************************************

class DownloadManager:
    def __init__(self, master,arquivo):
        self.master1 = master
        self.master1.title("Gerenciador de Downloads")

        self.arquivo = arquivo
        
        # Botão para selecionar a pasta de destino
        self.selecionar_pasta_button = tk.Button(self.master1, text="Selecione a Pasta Onde Será Realizado o Download", command=self.selecionar_pasta).pack(pady=10)
        
        # Label para exibir o caminho da pasta selecionada
        self.caminho_pasta_label = tk.Label(self.master1, text="Caminho da Pasta:").pack(pady=10)
        
        # Botão para iniciar o download
        self.iniciar_download_button = tk.Button(self.master1, text="Iniciar Download", command=self.iniciar_download).pack(pady=10)

        # self.master1.destroy()

    def selecionar_pasta(self):
        # try:
        # Abrir a janela para selecionar a pasta
        self.caminho_pasta = filedialog.askdirectory(title="Selecione a Pasta de Destino")
        
        # Verificar se uma pasta foi selecionada
        # if self.caminho_pasta:
        #     self.caminho_pasta_label.config(text=f"Caminho Selecionado: {self.caminho_pasta}")
        # else:
        #     print("Nenhuma pasta selecionada.")
        # except Exception as e:
        #     print(f"Erro ao selecionar pasta: {str(e)}")

    def iniciar_download(self):
        pd.DataFrame(self.arquivo, columns=("Ambiente", "tarefas")).to_excel(f'{self.caminho_pasta}/tarefas_executadas.xlsx', index=False)
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
