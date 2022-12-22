from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegisterUserView.as_view(), name='registration'),
    path('about/', about, name='about'),
    path('products/', Products.as_view(), name='products'),
    path('profile/', Products.as_view(), name='products'),
]
