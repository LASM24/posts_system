from django.contrib.auth.forms import UserCreationForm
from django.forms import BaseModelForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms


# Create your views here.
class SingUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        # modificar los estilos de los inputs en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-us us', 'placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-pass ps1', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-pass ps2', 'placeholder':'Repite la contraseña'})
        return form
