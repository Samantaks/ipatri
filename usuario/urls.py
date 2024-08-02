from django.urls import path
from .views import *


urlpatterns = [
    path('login/', loginpage, name='login-page'),
    path('cadastro/', cadastropage, name='cadastro-page'),
    path('app/profile', bio, name='user-page'),
]