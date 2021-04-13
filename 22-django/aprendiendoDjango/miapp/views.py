from django.shortcuts import render, HttpResponse

layout ="""
    <h1>Sitio Web Django</h1>
    <hr/>
    <ul>
        <li>
            <a href='/inicio'>Inicio</a>
        </li>
        <li>
            <a href='/hola-mundo'>Hola Mundo</a>
        </li>
        <li>
            <a href='/pagina-pruebas'>Pruebas</a>
        </li>
        <li>
            <a href='/contacto'>Contacto</a>
        </li>
    </ul>
    <hr/>
"""

# Create your views here.
def index(request):
    html = """
        <h1>Inicio</h1>
        <p>Año hasta el 2050:</p>
        <ul>
    """
    year = 2021
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"

    return HttpResponse(layout+html)

def hola_mundo(request):
    return HttpResponse(layout+"Hola mundo con Django!!!!")

def pagina(request):
    return HttpResponse(layout+"""
    <h1>pagina d emi web</h1>
    """)

def contacto(request,nombre='nombre'):
    return HttpResponse(layout+f"""
    <h2>Contacto {nombre}</h2>
    """)
