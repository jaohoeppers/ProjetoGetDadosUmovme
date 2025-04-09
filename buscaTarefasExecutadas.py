from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException,ElementClickInterceptedException,StaleElementReferenceException
from time import sleep

class buscadorTarefas:

    def __init__(self, navegador: webdriver, timeOut: int, diaFinal:int, meses_atras:int):
        self.__navegador = navegador
        self.__timeOut = timeOut
        self.__diaFinal = diaFinal
        self.__meses_atras = meses_atras

    @property
    def navegador(self):
        return self.__navegador
    
    @property
    def timeOut(self):
        return self.__timeOut
    
    @property
    def diaFinal(self):
        return self.__diaFinal
    
    @property
    def meses_atras(self):
        return self.__meses_atras

    def entrarPagina(self,url):
        try:
            self.navegador.get(url)
        except TimeoutException:
            print("Não foi possivel entrar na pagina")
        

    def logar(self,user,password):
        #Seta a senha e o login e clica em enviar
        WebDriverWait(self.navegador, self.timeOut).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(user)
        WebDriverWait(self.navegador, self.timeOut).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(password)
        self.clicar("submit_button")
        sleep(1)
        try:
            self.navegador.find_element(By.XPATH, "/html/body/div[@id='layout_content']/div[@class='nm-wrapper']/div/div/ul/li/span")
            return False
        except NoSuchElementException:
            return True

    def entraTarefas(self,url):
        #Tenta entrar nas tarefas 5 vezes, caso 
        for x in range(5):
            try:
                sleep(1)
                self.navegador.get(url+"schedule/search")
                sleep(1)
                break
            except TimeoutException:
                self.navegador.refresh()
                print(f'{x+1}° timeOut Entrando nas tarefas')
                continue

    def buscaDados(self):
        #clica no elemento para iniciar o preenchimento dos dados do mes/dia inicial da busca
        self.clicar("schedule_initialExecutionDate")
        for x in range(self.meses_atras):
            WebDriverWait(self.navegador, self.timeOut).until(EC.element_to_be_clickable((By.XPATH,"//a[@title='<Anterior']"))).click()
        diainicio = self.navegador.find_elements(By.XPATH,"//table/tbody/tr/td")
        for x in diainicio:
            if (x.text)!=" ":
                x.click()
                break
        #clica no elemento para iniciar o preenchimento dos dados do mes/dia final da busca
        self.clicar("schedule_finalExecutionDate")
        for x in range(self.meses_atras):
            WebDriverWait(self.navegador, self.timeOut).until(EC.element_to_be_clickable((By.XPATH,"//a[@title='<Anterior']"))).click()
        dias = self.navegador.find_elements(By.XPATH,"//table/tbody/tr/td")
        for x in dias:
            if (x.text)==f'{self.diaFinal}':
                x.click()
                break
        self.clicar("scheduleList_doSearch")

    def contarRegistros(self):
        #Tenta clicar no total de registros, caso não seja possivel, recarrega a página, busca os dados novamente e clica 
        try:
            self.clicar("forceCountRecordsLink")
        except ElementClickInterceptedException:
            self.navegador.refresh()
            self.buscaDados()
            self.clicar("forceCountRecordsLink")
        except TimeoutException:
            self.navegador.refresh()
            self.buscaDados()
            self.clicar("forceCountRecordsLink")
       
        # texto = str (self.navegador.find_element(By.XPATH,"//div[@style='float: right;']").text)
        try:
            self.rolar_ate_fim_pagina()
            texto = WebDriverWait(self.navegador, self.timeOut).until(
                EC.presence_of_element_located((By.XPATH, "//div[@style='float: right;']"))
            ).text
            texto = str(texto)
        except TimeoutException:
            print("Elemento não encontrado dentro do tempo limite.")
            texto = "0" 
            
        if texto=="Ver total de registros":
            return 0
        return int(texto[21:])
    
    def rolar_ate_fim_pagina(self):
        try:
            # Rola até o final da página
            self.navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Aguarda um tempo para garantir que o carregamento seja concluído
            sleep(2)
        except Exception as e:
            print(f"Erro ao rolar até o final da página: {e}")

    def clicar(self,idd):
        #Tenta clicar 5 vezes caso de erro de TimeOut
        for x in range(5):
            try:
                WebDriverWait(self.navegador, self.timeOut).until(EC.element_to_be_clickable((By.ID, idd))).click()
                break
            except TimeoutException:
                self.navegador.refresh()
                print(f"{x+1}° timeOut Clicando")
                continue
            except StaleElementReferenceException:
                self.navegador.refresh()
                print(f"{x+1}° Erro Clicando, {idd} não existe")
                continue
            except ElementClickInterceptedException:
                sleep(1)
                continue
            
#EXEMPLO DE USO DO BUSCADOR
# class main:
    # listaAmbientes= [
    #     '2rdistribuidora',
    #     '6f',
    #     'acaidguste',
    #     'acwgestaodeentregas',
    #     'aerotaio'
    # ]

    # listaTarefas=[]

# opcoes = Options()

# opcoes.add_argument('window-size=1366,900')
# navegador = webdriver.Edge(options=opcoes)

# tarefas = bt(navegador,10,30)

# for x in listaAmbientes:
#     tarefas.entrarPagina(f"https://{x}.umov.me/CenterWeb/")
#     if not tarefas.logar('master','SNNX917'):
#         print(f'Não foi possivel acessar o ambiente {x}, senha ou login incorretos')
#         continue
#     tarefas.entraTarefas(f"https://{x}.umov.me/CenterWeb/")

#     #passar o ultimo dia do mês 
#     tarefas.buscaDados()

#     sleep(2)
#     valor = tarefas.contarRegistros()
#     listaTarefas.append([x,valor])
#     print(f"{x}: {valor}")

#     #exporta as tarefas para uma tabela do Excel
#     pd.DataFrame(listaTarefas, columns=("Ambiente", "tarefas")).to_excel('teste.xlsx', index=False)
