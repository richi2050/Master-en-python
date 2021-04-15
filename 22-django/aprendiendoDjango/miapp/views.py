from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article

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
    
    nombre = 'Ricardo Lugo'
    lenguajes = ['java', 'javascript', 'php', 'C']
    year = 2021
    hasta = range(year, 2051)
    

    return render(request,'index.html',{
        'nombre': nombre,
        'title': 'inicio',
        'mi_variable' : 'soy un dato que ets ane la vista',
        'lenguajes' : lenguajes,
        'years': hasta})

def hola_mundo(request):
    return render(request,'hola_mundo.html')

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio/')
        

    return render(request,'pagina.html',{
        'texto' :'',
        'lista' : [1,2,3,4,5]
    })

def contacto(request,nombre='nombre'):
    return HttpResponse(layout+f"""
    <h2>Contacto {nombre}</h2>
    """)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()
    return HttpResponse(f"Usuario creado: {articulo.title}")
