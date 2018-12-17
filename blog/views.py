from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .forms import PerroForm
from django.utils import timezone
from .models import Post, Perros
# Create your views here.
def post_list(request):
    perro = Perros.objects.all()
    context = {'perros':perro}
    return render(request, 'blog/index.html', {})
def formulario(request):
    return render(request, 'blog/formulario.html', {})
def Informacion(request):
    return render(request, 'blog/Informacion.html', {})
def galeria(request):
    perro = Perros.objects.all()
    context = {'perros':perro}
    return render(request, 'blog/galeria.html', context)
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'blog/index.html'


class SignInView(LoginView):
    template_name = 'blog/iniciar_sesion.html'
class SignOutView(LogoutView):
    pass

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('blog:inciar_sesion.html'))
        else:
            return redirect(reverse('blog:inciar_sesion.html'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'blog/inciar-sesion.html', args)
def new_perro(request):
    if request.method == "POST":
        form = PerroForm(request.POST)
        if form.is_valid():
            perros = form.save(commit=False)
            perros.author = request.user
            perros.save()
        return redirect('index')
    else:
        form = PerroForm()
    return render(request, 'blog/index.html', {'form': form})