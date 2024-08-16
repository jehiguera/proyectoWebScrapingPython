#Webscrapping example to read online journals
#Jhiguera@ieee.org
#16/08/2024

from bs4 import BeautifulSoup
import requests

#url = 'https://elpais.com/educacion/2024-03-21/guia-para-no-perderse-en-los-nuevos-criterios-para-ser-profesor-titular-universitario-o-catedratico.html'
url = 'https://cincodias.elpais.com/companias/2024-08-16/la-galaxia-startup-un-sector-de-100000-millones-que-busca-su-hueco-en-la-economia-espanola.html'
try:
    response = requests.get(url)
    response.raise_for_status()  # Para manejar errores HTTP
except requests.exceptions.RequestException as e:
    print("Error al hacer la solicitud HTTP:", e)
    exit()

soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all(class_='a_c clearfix')

with open('output_journal.txt', 'w', encoding='utf-8') as ficheroNoticia2:
    for quote in quotes:
        ficheroNoticia2.write(quote.text.strip() + '\n')  # Añadir nueva línea después de cada cita
