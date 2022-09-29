from django.http import HttpResponse
from datetime import datetime
from django.template import context, Template

def view(request):
    return HttpResponse('Hello world')

def fecha(request):
    return HttpResponse(datetime.now())

def mi_template(request):
    cargar_archivo = open(r'C:\Users\RTECH\OneDrive\Documents\Mi pagina\mi_template\mi_template.html', 'r')

    template = Template(cargar_archivo.read())

    cargar_archivo.close()

    contexto = context()

    template_render = template.render(contexto)

    return HttpResponse(template_render)

