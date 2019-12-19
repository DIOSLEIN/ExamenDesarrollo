from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'gestion_usuario'

urlpatterns = [
    url('registrar/', views.registrar, name='registrar'),
    url('login/', views.usuario_login, name='login'),
    url('logout/', views.usuario_logout, name='logout'),
    path('add', views.add, name= 'add'),
    path('listar',views.listar, name='listar'),
    
    
    
    url('', views.index, name='index')
]
