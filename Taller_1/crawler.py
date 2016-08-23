from bs4 import BeautifulSoup
import requests
import re

url = "http://www.uniandes.edu.co/institucional/facultades/facultades"

req = requests.get(url)
statusCode = req.status_code

patron = re.compile('item[0-9]')

if statusCode == 200:
    html = BeautifulSoup(req.text)
    facultades = html.find_all('ul', {'class': 'menu_ifactum'})

    for facultad in facultades:
        lista = facultad.find_all('li',{'class': patron})
        for a in lista:
            enlaces = a.find_all('a', href=True)
            for enlace in enlaces:
                url = enlace.attrs['href']
                nombre = enlace.text
                print ("nombre: " + nombre + " url: " + url)
            break

else:
    print ("Status Code %d" %statusCode)
