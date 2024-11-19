# -> objetivo: realizar uma busca por produtos no site do mercado livre e retornar os links dos produtos

import requests
from bs4 import BeautifulSoup
import time

def printa(produto,tipo,classe,atributo):
    if(produto.find(f'{tipo}', attrs={f'{classe}':f'{atributo}'})):
        return produto.find(f'{tipo}', attrs={f'{classe}':f'{atributo}'}).text
    else: return ""

urlBase = 'https://lista.mercadolivre.com.br/'

# produto = input('Qual o produto desejado? ')
produto = 'furadeira'

response = requests.get(urlBase + produto)

# print(urlBase + produto)

site = BeautifulSoup(response.text , 'html.parser')

#procurando o produto todo
while True:
    produtos = site.findAll('div', attrs={'class':'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated'})
    if produtos:
        break

# print(produto2.text)
# time.sleep(2)

for x in produtos:
    # print(x.prettify())

#procurando somente a parte com os dados do produto
    while True:
        produto3 = x.find('div', attrs={'class': 'ui-search-result__content-wrapper'})
        if produto3:
            break
    
    # time.sleep(2)

# print(produto3.prettify())

#pegando o titulo, link e montando o preço do produto
    tituloProduto = produto3.find('a',attrs={'class':'ui-search-link__title-card ui-search-link'})
    link = tituloProduto['href']
    cifrao = printa(produto3,'span','class','andes-money-amount__currency-symbol')
    inteiro = printa(produto3,'span','class','andes-money-amount__fraction')
    centavos = printa(produto3,'span','class','andes-money-amount__cents andes-money-amount__cents--superscript-24')
    valor = cifrao+': '+inteiro+','+centavos

    print(tituloProduto['title'])
    print(link)
    print(valor + "\n")



