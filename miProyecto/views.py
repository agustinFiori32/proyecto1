from importlib.abc import Loader
from random import Random, random
from unittest import loader
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template
from django.template import loader

from home.models import persona

def view(request):
    return HttpResponse('Hello world')

def fecha(request):
    return HttpResponse(datetime.now())

def mi_template(request):
    cargar_archivo = open(r'C:\Users\RTECH\OneDrive\Documents\Mi pagina\miProyecto\mi_template\mi_template.html', 'r')

    template = Template(cargar_archivo.read())

    cargar_archivo.close()

    contexto = Context()

    template_render = template.render(contexto)

    return HttpResponse(template_render)

def tu_template(request,nombre):
    cargar_archivo = open(r'C:\Users\RTECH\OneDrive\Documents\Mi pagina\miProyecto\mi_template\mi_template.html', 'r')

    template = Template(cargar_archivo.read())

    cargar_archivo.close()

    contexto = Context({'persona' : nombre})

    template_render = template.render(contexto)

    return HttpResponse(template_render)

def familiares(request):
    cargar_archivo2 = open(r'C:\Users\RTECH\OneDrive\Documents\Mi pagina\miProyecto\mi_template\familiares.html', 'r')

    template_2 = Template(cargar_archivo2.read())

    cargar_archivo2.close()

    contexto = Context()

    template_render_2 = template_2.render(contexto)

    return HttpResponse(template_render_2)

def crear_persona(request, nombre, apellido):

    cargar_archivo = open(r'C:\Users\RTECH\OneDrive\Documents\Mi pagina\miProyecto\mi_template\crear_persona.html', 'r')

    template = Template(cargar_archivo.read())

    cargar_archivo.close()

    import random

    Persona = persona(nombre=nombre,apellido=apellido, edad= random.randrange(0,99), fecha_nacimiento=datetime.now())
    Persona.save()

    contexto = Context({'persona' : Persona})

    template_render = template.render(contexto)


    return HttpResponse(template_render)


def ver_persona(request):

    cargar_archivo = open(r'C:\Users\RTECH\OneDrive\Documents\Mi pagina\miProyecto\mi_template\ver_persona.html', 'r')

    template = Template(cargar_archivo.read())

    cargar_archivo.close()

    personas = persona.objects.all()

    contexto = Context({'personas' : personas})

    template_render = template.render(contexto)

    return HttpResponse(template_render)


