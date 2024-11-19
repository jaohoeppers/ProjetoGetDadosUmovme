from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep

opcoes = Options()
#utilizado para que a janela não apareca
# opcoes.add_argument('--haedless')

#define o tamanho da janela para 1080x720
opcoes.add_argument('window-size=1080,720')

#Abre o navegador escolhido com as opções passadas
navegador = webdriver.Chrome(options=opcoes)

#Abre a pagina especifica 
navegador.get("https://testemaster.umov.me/CenterWeb/")

#Aguarda alguns segundos ate a pagina carregar
sleep(2)

#É utilizado para visualizar o conteudo html da pagina 'navegador.page_source'
# print(BeautifulSoup(navegador.page_source, 'html.parser').prettify())

#Busca um elemento na pagina de acordo com o ID dele
usuario = navegador.find_element(By.ID,'username')
senha = navegador.find_element(By.ID,'password')
botao = navegador.find_element(By.ID,'submit_button')

#Adiciona um valor no campo aberto
usuario.send_keys('master')
senha.send_keys('SNNX917')

#Envia o valor digitado
# usuario.submit()

#Clica no botão de enviar
botao.click()




sleep(20)
