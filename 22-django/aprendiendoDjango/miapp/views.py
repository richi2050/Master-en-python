from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q

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
    return HttpResponse(f"Articulo creado: {articulo.title}")

def save_article(request):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title}")

def create_article(request):
    return render(request, 'create_article.html')


def articulo(request):
    articulo = Article.objects.get(id=3)
    #articulo = Article.objects.get(pk=7)
    #articulo = Article.objects.get(title='articloURL', public= True)
    try:
        articulo = Article.objects.get(id=3)
        response= f"Articulo: { articulo.title }"
    except:
        response = "<h1>Articulo no encontrado </h1>"
    return HttpResponse(response)

def edit_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title ='titulo modificado'
    articulo.content='este es el contenido modificado'
    articulo.public = True
    articulo.save()
    return HttpResponse(f"Articulo editado: {articulo.title}")

def articulos(request):
    articulos = Article.objects.all();
    #articulos = Article.objects.order_by('-title'); #orderby ASC
    #articulos = Article.objects.order_by('title'); #orderby DESC
    #articulos = Article.objects.order_by('title')[:2]; #que solo aparezca un elemento
    #articulos = Article.objects.order_by('title')[1:2]; #que solo aparezca un elemento de rango 1:2
    #---------------------------  filter y lookups  ----------------------------------
    #articulos = Article.objects.filter(title='articloURL',id=5) where
    #articulos = Article.objects.filter(title__contains='Primer') #like
    articulos = Article.objects.filter(title__exact='articloURL') #exacto
    articulos = Article.objects.filter(title__iexact='articloURL') #exacto peor no distingue entre mayusculas y minusculas
    articulos = Article.objects.filter(id__gt=2) #solo que busca mayor que gt
    articulos = Article.objects.filter(id__gte=2) #solo que busca mayor he igua es que gt

    articulos = Article.objects.filter(id__lt=2) #solo que busca menores que lt
    articulos = Article.objects.filter(id__lte=2) #solo que busca menores he iguales que gt
    articulos = Article.objects.all().exclude(public=True)
    articulos = Article.objects.raw("SELECT * FROM miapp_article where public=True")

    # OR en consultas con el ORM
    articulos = Article.objects.filter(
        Q(title__contains='1') | Q(title__contains='3') 
    )

    return render(request, 'articulos.html', {
        'articulos': articulos
    })
def borrar_articulo(request,id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')