import requests
from bs4 import BeautifulSoup
from testes.seleniumTeste import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(session, base_url, login, senha):
    login_url = f"{base_url}/login"
    data = {'username': login, 'password': senha}
    response = session.post(login_url, data=data)
    return response.status_code == 200

def coletar_dados(session, base_url, filtro):
    pagina_url = f"{base_url}/"+filtro
    response = session.get(pagina_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Exemplo de como encontrar um elemento específico
    dados = soup.find('div', class_='footer-poweredby',)
    return dados.text.strip() if dados else None

def coletar_dados_multiplos_sites():
    sites = [
        {
            'base_url': 'http://exemplo.com',
            'ambiente': 'ambiente1',
            'login': 'usuario1',
            'senha': 'senha1',
            'filtro': 'filtro1'
        },
        {
            'base_url': 'http://outroexemplo.com',
            'ambiente': 'ambiente2',
            'login': 'usuario2',
            'senha': 'senha2',
            'filtro': 'filtro2'
        }
    ]

    session = requests.Session()

    for site in sites:
        base_url = site['base_url']
        ambiente = site['ambiente']
        login = site['login']
        senha = site['senha']
        filtro = site['filtro']

        # Realizar o login
        if login(session, base_url, ambiente, login, senha):
            print(f"Login bem-sucedido para {base_url}")
            
            # Coletar dados da página específica
            dados = coletar_dados(session, base_url, filtro)
            if dados:
                print(f"Dados coletados com sucesso de {base_url}:")
                print(dados)
            else:
                print(f"Não foi possível coletar dados de {base_url}")
        else:
            print(f"Falha ao tentar logar em {base_url}")

# Executar a função principal
# coletar_dados_multiplos_sites()

session = requests.Session()
base = "https://testemaster.umov.me/CenterWeb"

filtro = ""

print(login(session,base,"master","SNNX917"))
print("deu")
print(coletar_dados(session,base,filtro))
print("deu2")
