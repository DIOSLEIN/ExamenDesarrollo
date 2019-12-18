from django import forms
from django.contrib.auth.models import User
from .models import PerfilUsuario
from .models import Producto

class RegistrarProducto(forms.ModelForm):
    class Meta():
        model = Producto
        fields = ('nombreProducto',
                'precioProducto',
                'cantidad',
                )
        labels = {
            'nombreProducto': 'Nombre',
            'precioProducto': 'Valor',
            'cantidad': 'Cantidad',
        }

    # Define el class="form-control" en los labels del formulario
    def init(self, args, **kwargs):
        super(RegistrarProducto, self).__init__(args, **kwargs)
        self.fields['nombreProducto'].widget.attrs.update({'class': 'form-control'})
        self.fields['precioProducto'].widget.attrs.update({'class': 'form-control'})
        self.fields['cantidad'].widget.attrs.update({'class': 'form-control'})


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