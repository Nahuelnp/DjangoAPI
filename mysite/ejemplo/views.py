from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse




# Create your views here.
def index(request):
    return HttpResponse("Hola desde mi primer Vista")


def miVista(required):

    doc_externo=open("C:/Users/Nahuel/Desktop/ejercicios programacion/vue js/Vue ex/index.html")
    
    plt=Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx=Context()

    documento= plt.render(ctx)

    return HttpResponse(documento)
