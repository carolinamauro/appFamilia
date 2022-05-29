from AppFamilia.models import Persona
import datetime

def crear_persona(nombre,apellido,año,mes,dia):

    nacimiento_persona = datetime.date(año,mes,dia)
    persona = Persona(nombre = nombre, apellido = apellido, nacimiento = nacimiento_persona)
    persona.save()

    return persona



