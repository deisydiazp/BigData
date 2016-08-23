from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re

# Create your views here.
from Taller_1.models import UnidadAcademica


def inicio(request):
    return render (request,"inicio.html",{})

def taller1_getUnidadesAcademicas(request):

    listaUnidades = crawler_unidadesAcademicas()
    return render (request,"taller1_unidadesAcademicas.html",{'listaUnidades': listaUnidades})


def crawler_unidadesAcademicas():

    url = "http://www.uniandes.edu.co/institucional/facultades/facultades"

    req = requests.get(url)
    statusCode = req.status_code

    patron = re.compile('item[0-9]')

    listaUnidades = []

    if statusCode == 200:
        html = BeautifulSoup(req.text)
        facultades = html.find_all('ul', {'class': 'menu_ifactum'})

        for facultad in facultades:
            lista_li = facultad.find_all('li', {'class': patron})
            for lista_a in lista_li:
                enlaces = lista_a.find_all('a', href=True)
                for enlace in enlaces:
                    ua = UnidadAcademica(nombre=enlace.text,url=enlace.attrs['href'])
                    listaUnidades.append(ua)
                break

    else:
        print("Status Code %d" % statusCode)

    return listaUnidades