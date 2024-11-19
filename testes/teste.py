import requests
from bs4 import BeautifulSoup
import pandas as pd

#https://github.com/walissonsilva/web-scraping-python

#Faz o request para pegar os dados que existem na pagina
site = requests.get("https://www.nauber.com.br/")

# print("Status code", site.status_code)
# print("Header site", site.headers)
# print("Conteudo site", site.content)

#Salva o body da pagina na variavel
conteudo = site.content

#Gera um objeto do tipo BeatifulSoup e passa o conteudo da pagina para ela
conteudo2 = BeautifulSoup(conteudo, "html.parser")

#Prettify deixa as tags e divs tabuladas corretamente
# print(conteudo2.prettify)

#Realiza uma busca no conteudo da variavel conteudo2, 
#Esta buscando uma div que contenha o atributo 'class' = col-lg-8 col-md-8 col-sm-8 col-xs-12
#Podemos utilizar o metodo findall para pegar todas as divs que contenham a classe ...
meio = conteudo2.find('div', attrs={'class' : 'col-lg-8 col-md-8 col-sm-8 col-xs-12'})

#Busca um p dentro de 'meio'
texto = meio.find('p')

itens = conteudo2.find('div', attrs={'class': 'news-area section-space-88-100'})

# print(itens)
containers = itens.findAll('div', attrs={'class' : 'container'})

x = containers[1]

i1 = x.findAll('div', attrs={'class': 'inner-news-box-bottom'})

lista=[]

for x in i1:
    t1 = x.find('h4')
    t2 = x.find('p')
    # print(t1.text)
    # print(t2.text)
    # print()
    lista.append([t1.text, t2.text])

# print(lista[0][0].text)
# print(lista[0][1]['href'])

noticias = pd.DataFrame(lista, columns=("Local", "Noticia"))

noticias.to_excel('teste.xlsx', index=False)

# print(noticias)


# it = x.find('div', attrs={'class': 'owl-item active'})
# it2 = item.find('p')

# print(it2.text)


# print(meio.text)