from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
    
        widgets = {
            "fecha_fabricacion":forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    pass