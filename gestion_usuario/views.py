from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import RegistrarForm, PerfilUsuarioForm,ProductoForm, Producto

# Cierre de sesion

def dolar(request):
    return render(request, 'presupuestador/api_dolar.html', {})

def usuario_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('gestion_usuario:index'))

def index(request):
    return render(request, 'gestion_usuario/index.html', {})    
       

def usuario_login(request): 
    # Valida si existe un usuario autenticado
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse, ('gestion_usuario:index'))
    else:
        # Recibe formulario mediante metodo POST
        if request.method == 'POST':
            # Recibimos la informacion del formulario
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Autenticamos el usuario
            user = authenticate(username=username, password=password)
            # Verifica que exista el usuario
            if user:
                # Verifica si el usuario esta activo
                if user.is_active:
                    # Genera un login para autenticar al usuario
                    login(request, user)
                    return HttpResponseRedirect(reverse('gestion_usuario:index'))
                else:
                    return HttpResponse("Tu cuenta esta inactiva.")
            else:
                # Si no existe usuario
                print("username: {} - password: {}".format(username, password))
                return HttpResponse("Datos inválidos")
        else:  # Si llega desde una url en metodo GET (desde el navegador)
            return render(request, 'gestion_usuario/login.html', {})

def registrar(request):
    registrado = False
    # Recibe formulario mediante metodo POST
    if request.method == 'POST':
        # Crea formulario de usuario con informacion del request
        user_form = RegistrarForm(data=request.POST)
        # Crea formulario de perfil con informacion del request
        profile_form = PerfilUsuarioForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Guardamos en base de datos
            user = user_form.save()
            # Encripta password con el modelo de django
            user.set_password(user.password)
            # Guarda usuario tras encriptacion
            user.save()
            # Instancia un objeto perfil
            profile = profile_form.save(commit=False)
            # Asigna un usario al perfil
            profile.user = user
            # Valida si en el Array FILES existe el archivo del input foto_perfil
            if 'foto_perfil' in request.FILES:
                # Agrega la imagen al perfil
                profile.foto_perfil = request.FILES['foto_perfil']
            # Guarda en base de datos
            profile.save()
            registrado = True
        else:  # Si alguno de los formularios es invalido
            print(user_form.errors, profile_form.errors)
            return HttpResponse("Datos inválidos")
    else:  # Si no es POST generamos los formularios
        user_form = RegistrarForm()
        profile_form = PerfilUsuarioForm()

    return render(request, 'gestion_usuario/registrar.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registrado': registrado})

 
def listar(request):
    if request.user.is_authenticated:
        # creamos una colección la cual carga TODOS los registos
        productos = Producto.objects.all()
        # renderizamos la colección en el template
        return render(request,
            "presupuestador/listar.html", {'productos': productos})
    else:
        return render(request, 'principal.html', {})

def add(request):
    # Creamos un formulario vacío
    form = ProductoForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = ProductoForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return redirect('presupuestador/listar.html')
            

    # Si llegamos al final renderizamos el formulario
    return render(request, "presupuestador/add.html", {'form': form})

