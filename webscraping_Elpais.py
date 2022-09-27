#Ejemplo para hacer web scrapping en la web de www.elpais para descargar noticias que no se pueden leer sin estar con la suscripcion de pago
#Jhiguera@ieee.org
#06/08/2022

from http.cookies import _quote
from smtplib import quotedata
import requests
from bs4 import BeautifulSoup
ficheroNoticia2 = open('Elpais3.txt','w', encoding='utf-8')
#url = 'https://elpais.com/internacional/2022-08-06/taiwan-acusa-a-china-de-simular-un-ataque-a-la-isla.html/'
#url = 'https://elpais.com/actualidad/newsletter-kiko-llaneras/2022-08-06/dime-cuanto-ganan-tus-amigos-y-te-dire-lo-pobre-o-rico-que-eres-tu.html/'
#url = 'https://elpais.com/television/2022-08-10/jandro-mago-en-la-television-te-entierran-enseguida.html/'
url = 'https://elpais.com/ciencia/2022-09-27/como-sabemos-si-el-impacto-de-la-sonda-dart-movio-realmente-el-asteroide.html'

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
 