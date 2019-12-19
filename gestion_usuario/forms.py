from django import forms
from django.contrib.auth.models import User
from .models import PerfilUsuario
from .models import Producto
from django.forms import ModelForm




class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombreproducto','precioproducto','costopresupuestado','tienda','nota']
        labels = {
            'nombreproducto': 'Nombre del Producto',
            'precioproducto': 'Precio',
            'costopresupuestado': 'Costo presupuestado',
            'tienda':'Local procedencia',
            'nota': 'Comentario',
        }
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['nombreproducto'].widget.attrs.update({'class': 'form-control'})
        self.fields['precioproducto'].widget.attrs.update({'class': 'form-control'})
        self.fields['costopresupuestado'].widget.attrs.update({'class': 'form-control'})   
        self.fields['tienda'].widget.attrs.update({'class': 'form-control'})
        self.fields['nota'].widget.attrs.update({'class': 'form-control'}) 
                
                
       

    


class   PerfilUsuarioForm(forms.ModelForm):
    class Meta():
        model = PerfilUsuario
        fields = ('foto_perfil',)
        # Labels nos cambia el texto del label que corresponde al input
        labels = {
            'foto_perfil': 'Foto de perfil'
        }

class RegistrarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    class Meta:
        model = User
        fields = ('username', 
                'email', 
                'password')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo',
            'password': 'Contraseña'
        }
        help_texts = {
            'username': '',
        }
        error_messages = {
            'username': {
                'max_length': 'Maximo 150 caracteres',
                'required': 'Requerido'
            },
            'password': {
                'required': 'Requerido'
            }
        }

    # Define el class="form-control" dentro de los labels del formulario
    def __init__(self, *args, **kwargs):
        super(RegistrarForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})