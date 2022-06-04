from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://gutoffline.github.io/site-turismo/"
resposta = urlopen(url)
html_site = resposta.read()

#print(html_site)
soup_site = BeautifulSoup(html_site,"html.parser")
#print(soup_site.prettify())

#Pegar o título da página
titulo_aba = soup_site.title.get_text()
print(titulo_aba)

cabecalho_principal = soup_site.body.div.h1.a.get_text()
print(cabecalho_principal)

rancho = soup_site.body.div.div.div.h2.get_text()
print(rancho)

lista_lugares = soup_site.select(".lateral")
print(lista_lugares)
