from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
        <h1>Inicio</h1>
    """)

def hola_mundo(request):
    return HttpResponse("Hola mundo con Django!!!!")

def pagina(request):
    return HttpResponse("""
    <h1>pagina d emi web</h1>
    """)
