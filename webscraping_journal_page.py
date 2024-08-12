#Example to do web scrapping on the web of an online news newspaper
#Jhiguera@ieee.org
#12/08/2024

from http.cookies import _quote
from smtplib import quotedata
import requests
from bs4 import BeautifulSoup
ficheroNoticia2 = open('journal_news.txt','w', encoding='utf-8')
#url = 'https://elpais.com/internacional/2022-08-06/taiwan-acusa-a-china-de-simular-un-ataque-a-la-isla.html/'
#url = 'https://elpais.com/actualidad/newsletter-kiko-llaneras/2022-08-06/dime-cuanto-ganan-tus-amigos-y-te-dire-lo-pobre-o-rico-que-eres-tu.html/'
#url = 'https://elpais.com/educacion/2024-03-21/guia-para-no-perderse-en-los-nuevos-criterios-para-ser-profesor-titular-universitario-o-catedratico.html'
url = 'https://elpais.com/ideas/2024-08-12/para-que-tenemos-amigos-de-segundo-rango.html'

response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
#quotes = soup.find_all('span',class_='text') #ejemplo de una web sin seguridad
#quotes = soup.find_all(class_='a_st')#titulo
#quotes = soup.find_all(class_='a_c clearfix') #contenido
quotes = soup.find_all(class_='a_c clearfix')
for quote in quotes:
    print(str(quote.text)) #Importante hay que convertir el contendio a string para evitar errores sobre todo cuando hay tablas en el texto
    #if quote.text == str:
    ficheroNoticia2.write(quote.text)


ficheroNoticia2.close()
 