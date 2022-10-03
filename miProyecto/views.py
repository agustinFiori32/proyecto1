from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template

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


