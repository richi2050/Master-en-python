from django.shortcuts import render, HttpResponse

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

    return HttpResponse(html)

def hola_mundo(request):
    return HttpResponse("Hola mundo con Django!!!!")

def pagina(request):
    return HttpResponse("""
    <h1>pagina d emi web</h1>
    """)
