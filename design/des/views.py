from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from .forms import RegisterUserForm
from .models import Products, User


class Index(generic.ListView):
    model = Products
    template_name = 'index.html'


class RegisterUserView(CreateView):
    template_name = 'registration/regist.html'
    success_url = reverse_lazy('login')
    form_class = RegisterUserForm


def about(request):
    return render(request, 'about_us.html')

# class About(generic.ListView):
#     template_name = 'about_us.html'


class Products(generic.ListView):
    model = Products
    template_name = 'products.html'


class Profile(generic.ListView):
    model = User
    template_name = 'profile.html'
