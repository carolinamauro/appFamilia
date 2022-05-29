from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import render
from AppFamilia.funciones import crear_persona
from django.template import loader

def familia(self):


    caro = crear_persona("Carolina","Mauro",2003,4,7)
    coni = crear_persona("Constanza","Mauro",2001,1,11)
    ale = crear_persona("Ale","DiPrinzio",1965,10,8)
    diccionario = {"caro": caro,"coni": coni,"ale": ale}

    plantilla1 = loader.get_template('plantilla1.html')
    documento = plantilla1.render(diccionario)

    return HttpResponse(documento)



